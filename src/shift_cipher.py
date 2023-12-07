from vlads_stupid_crypto_lib.src.helpers import map_to_26, map_to_letter, ALPHABET_SIZE

class ShiftCipher():

    def __init__(self, text, shift_value=3, preserve_spaces=True):
        self.shift_value = shift_value % ALPHABET_SIZE
        self.text = text.upper()
        self.preserve_spaces = preserve_spaces
    
    def encrypt(self) -> str:
        self._shift(True)
        return self.text if self.preserve_spaces else self.text.replace(" ", "")

    def decrypt(self) -> str:
        self._shift(False)
        return self.text
    
    def _shift(self, encrypt_flag=True) -> None:
        ordinal_list = map_to_26(self.text)
        return_text = ""
        for i in range(0, len(ordinal_list)):
            if (ordinal := ordinal_list[i]) != -1:
                temp_shift_value = self._get_temp_shift_value(ordinal, encrypt_flag) 
                return_text += map_to_letter(ordinal + temp_shift_value)
            else:
                return_text += self.text[i]
        self.text = return_text
    
    def _get_temp_shift_value(self, ordinal, encrypt_flag=True) -> int:
        if encrypt_flag:
            return self.shift_value 
        return -self.shift_value if ordinal - self.shift_value >= 0 else -(ALPHABET_SIZE - (self.shift_value - ordinal))