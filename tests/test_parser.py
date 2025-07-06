# tests/test_parser.py

import unittest
from parser.log_parser import parse_log_line

class TestLogParser(unittest.TestCase):
    def test_valid_failed_login(self):
        line = "Jul  6 10:23:44 ubuntu sshd[24562]: Failed password for invalid user admin from 192.168.1.101 port 45522 ssh2"
        parsed = parse_log_line(line)
        self.assertIsNotNone(parsed)
        self.assertEqual(parsed["username"], "admin")
        self.assertEqual(parsed["ip_address"], "192.168.1.101")
        self.assertEqual(parsed["event_type"], "failed_login")
        self.assertEqual(parsed["user_type"], "invalid_user")

    def test_non_matching_line(self):
        line = "This is some random log that doesn't match"
        parsed = parse_log_line(line)
        self.assertIsNone(parsed)

if __name__ == "__main__":
    unittest.main()
