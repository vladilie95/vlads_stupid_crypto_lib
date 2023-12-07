from vlads_stupid_crypto_lib.src.shift_cipher import ShiftCipher
from pytest import mark

@mark.parametrize(
        "plaintext_value, shift_value, expected_ciphertext, preserve_spaces",
        [
            ("abcDEF55_a", 1, "BCDEFG55_B", True),
            ("some string with spaces", 0, "SOME STRING WITH SPACES", True),
            ("some string with spaces", 0, "SOMESTRINGWITHSPACES", False),
            ("aaaaa", 100, "WWWWW", False),
        ]
)
def test_shift_cipher(plaintext_value, shift_value, expected_ciphertext, preserve_spaces):
    shift_cipher = ShiftCipher(plaintext_value, shift_value, preserve_spaces)
    assert shift_cipher.encrypt() == expected_ciphertext
    assert shift_cipher.decrypt() == plaintext_value.upper()



