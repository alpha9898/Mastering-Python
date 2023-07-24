class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        has_lowercase = any(c.islower() for c in password)
        has_uppercase = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special_char = any(c in "!@#$%^&*()-+" for c in password)

        if not (has_lowercase and has_uppercase and has_digit and has_special_char):
            return False

        for i in range(len(password) - 1):
            if password[i] == password[i + 1]:
                return False

        return True