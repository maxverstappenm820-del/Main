import time
import datetime
import sys
import os
import platform
import threading
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AlarmConfig:
    alarm_time: datetime.time
    label: str = "Alarm"
    snooze_duration: int = 5
    recurring: bool = False
    recurrence_days: list[str] = field(default_factory=list)


class AlarmClock:
    DAYS_OF_WEEK = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    def __init__(self):
        self._stop_event = threading.Event()
        self._snooze_event = threading.Event()

    def _play_sound(self) -> None:
        system = platform.system()
        if system == "Windows":
            import winsound
            for _ in range(5):
                winsound.Beep(1000, 600)
                time.sleep(0.2)
        elif system == "Darwin":
            os.system("afplay /System/Library/Sounds/Ping.aiff -t 3 2>/dev/null || say 'Alarm ringing'")
        else:
            for _ in range(5):
                sys.stdout.write("\a")
                sys.stdout.flush()
                time.sleep(0.5)

    def _display_countdown(self, target: datetime.datetime) -> None:
        while not self._stop_event.is_set():
            now = datetime.datetime.now()
            remaining = target - now
            if remaining.total_seconds() <= 0:
                break
            total_secs = int(remaining.total_seconds())
            hours, remainder = divmod(total_secs, 3600)
            minutes, seconds = divmod(remainder, 60)
            sys.stdout.write(
                f"\r  Current: {now.strftime('%H:%M:%S')}  |  "
                f"Target: {target.strftime('%H:%M:%S')}  |  "
                f"Remaining: {hours:02d}:{minutes:02d}:{seconds:02d}   "
            )
            sys.stdout.flush()
            time.sleep(1)

    def _get_next_trigger(self, alarm_time: datetime.time, recurrence_days: list[str]) -> datetime.datetime:
        now = datetime.datetime.now()
        today_trigger = datetime.datetime.combine(now.date(), alarm_time)

        if not recurrence_days:
            if today_trigger > now:
                return today_trigger
            return today_trigger + datetime.timedelta(days=1)

        day_indices = [self.DAYS_OF_WEEK.index(d) for d in recurrence_days]
        for offset in range(8):
            candidate = today_trigger + datetime.timedelta(days=offset)
            if candidate.weekday() in day_indices and candidate > now:
                return candidate

        raise ValueError("Could not determine next recurrence trigger.")

    def _ring_alarm(self, config: AlarmConfig) -> str:
        print(f"\n\n  *** {config.label.upper()} — ALARM RINGING! ***\n")
        sound_thread = threading.Thread(target=self._play_sound, daemon=True)
        sound_thread.start()

        print("  Options: [s] Snooze  |  [d] Dismiss")
        response = input("  Your choice: ").strip().lower()
        self._stop_event.set()
        sound_thread.join(timeout=2)
        return response

    def run(self, config: AlarmConfig) -> None:
        print(f"\n  Alarm '{config.label}' set for {config.alarm_time.strftime('%H:%M:%S')}", end="")
        if config.recurring:
            print(f" — repeats on: {', '.join(d.capitalize() for d in config.recurrence_days)}")
        else:
            print()

        while True:
            self._stop_event.clear()
            self._snooze_event.clear()

            target = self._get_next_trigger(config.alarm_time, config.recurrence_days)
            print(f"\n  Next trigger: {target.strftime('%A, %d %b %Y at %H:%M:%S')}\n")

            countdown_thread = threading.Thread(
                target=self._display_countdown, args=(target,), daemon=True
            )
            countdown_thread.start()

            while datetime.datetime.now() < target and not self._stop_event.is_set():
                time.sleep(0.5)

            self._stop_event.set()
            countdown_thread.join(timeout=2)

            response = self._ring_alarm(config)

            if response == "s":
                snooze_until = datetime.datetime.now() + datetime.timedelta(minutes=config.snooze_duration)
                print(f"\n  Snoozed for {config.snooze_duration} minute(s). Resuming at {snooze_until.strftime('%H:%M:%S')}.\n")
                self._stop_event.clear()
                snooze_thread = threading.Thread(
                    target=self._display_countdown, args=(snooze_until,), daemon=True
                )
                snooze_thread.start()
                while datetime.datetime.now() < snooze_until:
                    time.sleep(0.5)
                self._stop_event.set()
                snooze_thread.join(timeout=2)
                self._ring_alarm(config)

            if not config.recurring:
                print("\n  Alarm dismissed. Goodbye!\n")
                break

            print("\n  Recurring alarm dismissed. Waiting for next trigger...\n")


class AlarmSetup:
    @staticmethod
    def parse_time(time_str: str) -> Optional[datetime.time]:
        for fmt in ("%H:%M:%S", "%H:%M"):
            try:
                return datetime.datetime.strptime(time_str.strip(), fmt).time()
            except ValueError:
                continue
        return None

    @staticmethod
    def get_alarm_time() -> datetime.time:
        while True:
            raw = input("  Alarm time (HH:MM or HH:MM:SS): ").strip()
            parsed = AlarmSetup.parse_time(raw)
            if parsed:
                return parsed
            print("  Invalid format. Please use HH:MM or HH:MM:SS (24-hour).")

    @staticmethod
    def get_label() -> str:
        raw = input("  Label (press Enter for 'Alarm'): ").strip()
        return raw if raw else "Alarm"

    @staticmethod
    def get_snooze_duration() -> int:
        while True:
            raw = input("  Snooze duration in minutes (press Enter for 5): ").strip()
            if not raw:
                return 5
            if raw.isdigit() and 1 <= int(raw) <= 60:
                return int(raw)
            print("  Please enter a number between 1 and 60.")

    @staticmethod
    def get_recurrence() -> tuple[bool, list[str]]:
        answer = input("  Make this a recurring alarm? (y/N): ").strip().lower()
        if answer != "y":
            return False, []

        days_input = input(
            "  Enter days separated by commas\n"
            "  (e.g. monday,wednesday,friday — or press Enter for every day): "
        ).strip().lower()

        if not days_input:
            return True, AlarmClock.DAYS_OF_WEEK

        selected = [d.strip() for d in days_input.split(",")]
        valid = [d for d in selected if d in AlarmClock.DAYS_OF_WEEK]
        invalid = [d for d in selected if d not in AlarmClock.DAYS_OF_WEEK]

        if invalid:
            print(f"  Ignored unrecognized days: {', '.join(invalid)}")

        if not valid:
            print("  No valid days selected. Defaulting to every day.")
            return True, AlarmClock.DAYS_OF_WEEK

        return True, valid

    @classmethod
    def build_config(cls) -> AlarmConfig:
        print("\n  === Alarm Clock Setup ===\n")
        alarm_time = cls.get_alarm_time()
        label = cls.get_label()
        snooze_duration = cls.get_snooze_duration()
        recurring, recurrence_days = cls.get_recurrence()
        return AlarmConfig(
            alarm_time=alarm_time,
            label=label,
            snooze_duration=snooze_duration,
            recurring=recurring,
            recurrence_days=recurrence_days,
        )


def main() -> None:
    try:
        config = AlarmSetup.build_config()
        clock = AlarmClock()
        clock.run(config)
    except KeyboardInterrupt:
        print("\n\n  Alarm cancelled. Goodbye!\n")
        sys.exit(0)


if __name__ == "__main__":
    main()