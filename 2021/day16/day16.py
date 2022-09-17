class decoder():
    def __init__(self, hex_string):
        hex_integer = str(bin(int(hex_string, 16)))
        code = hex_integer.split("b")[1]
        while len(code) < len(hex_string) * 4:
            code = "0" + code
        self.code = code
        self.version_total = 0

    def run_type(self, type, remaining_code, arg1 = 10000):
        subs, steps = self.get_subs(remaining_code, arg1)
        if type == 0:
            val1 = sum(subs)
        elif type == 1:
            to_ret = 1
            for sub in subs:
                to_ret *= sub
            val1 = to_ret
        elif type == 2:
            val1 = min(subs)
        elif type == 3:
            val1 = max(subs)
        elif type == 5:
            val1 = 0
            if subs[0]>subs[1]:
                val1 = 1
        elif type == 6:
            val1 = 0
            if subs[0] < subs[1]:
                val1 = 1
        elif type == 7:
            val1 = 0
            if subs[0] == subs[1]:
                val1 = 1
        return val1, steps

    def get_subs(self, remaining_code, num_subs):
        subs = []
        step_bit = 0
        while True:
            val1, nexts = self.get_packet_val(remaining_code[step_bit:])
            subs.append(val1)
            step_bit += nexts
            if step_bit >= len(remaining_code):
                break
            if len(subs) >= num_subs:
                break
        return subs, step_bit

    def type_4(self, remaining_code):
        step_bit = 0
        lit_num = ""
        while True:
            if remaining_code[step_bit] == "1":
                step_bit += 1
                lit_num += remaining_code[step_bit:step_bit + 4]
                step_bit += 4
            elif remaining_code[step_bit] == "0":
                step_bit += 1
                lit_num += remaining_code[step_bit:step_bit + 4]
                step_bit += 4
                break
        return int(lit_num, 2), step_bit

    def get_packet_val(self, remaining_code):
        current_bit = 0
        packet_version = int(remaining_code[current_bit:current_bit + 3], 2)
        self.version_total += packet_version
        current_bit += 3
        type_id = int(remaining_code[current_bit:current_bit + 3], 2)
        current_bit += 3
        if type_id == 4:  # Literal
            rep_num, bit_skip = self.type_4(remaining_code[current_bit:])
            current_bit += bit_skip
            return rep_num, current_bit
        else:  # Operator Packet
            length_id = int(remaining_code[current_bit])
            current_bit += 1
            packet_length = 10000
            num_subs = 10000
            if length_id == 0:
                packet_length = int(remaining_code[current_bit:current_bit + 15], 2)
                current_bit += 15
            else:
                num_subs = int(remaining_code[current_bit:current_bit + 11], 2)
                current_bit += 11
            val1, bits_skipped = self.run_type(type_id, remaining_code[current_bit:current_bit+packet_length], num_subs)
        return val1, current_bit+bits_skipped
        print("Version total:", version_total)

decode = decoder("40541D900AEDC01A88002191FE2F45D1006A2FC2388D278D4653E3910020F2E2F3E24C007ECD7ABA6A200E6E8017F92C934CFA0E5290B569CE0F4BA5180213D963C00DC40010A87905A0900021B0D624C34600906725FFCF597491C6008C01B0004223342488A200F4378C9198401B87311A0C0803E600FC4887F14CC01C8AF16A2010021D1260DC7530042C012957193779F96AD9B36100907A00980021513E3943600043225C1A8EB2C3040043CC3B1802B400D3CA4B8D3292E37C30600B325A541D979606E384B524C06008E802515A638A73A226009CDA5D8026200D473851150401E8BF16E2ACDFB7DCD4F5C02897A5288D299D89CA6AA672AD5118804F592FC5BE8037000042217C64876000874728550D4C0149F29D00524ACCD2566795A0D880432BEAC79995C86483A6F3B9F6833397DEA03E401004F28CD894B9C48A34BC371CF7AA840155E002012E21260923DC4C248035299ECEB0AC4DFC0179B864865CF8802F9A005E264C25372ABAC8DEA706009F005C32B7FCF1BF91CADFF3C6FE4B3FB073005A6F93B633B12E0054A124BEE9C570004B245126F6E11E5C0199BDEDCE589275C10027E97BE7EF330F126DF3817354FFC82671BB5402510C803788DFA009CAFB14ECDFE57D8A766F0001A74F924AC99678864725F253FD134400F9B5D3004A46489A00A4BEAD8F7F1F7497C39A0020F357618C71648032BB004E4BBC4292EF1167274F1AA0078902262B0D4718229C8608A5226528F86008CFA6E802F275E2248C65F3610066274CEA9A86794E58AA5E5BDE73F34945E2008D27D2278EE30C489B3D20336D00C2F002DF480AC820287D8096F700288082C001DE1400C50035005AA2013E5400B10028C009600A74001EF2004F8400C92B172801F0F4C0139B8E19A8017D96A510A7E698800EAC9294A6E985783A400AE4A2945E9170")
total, num_bits_read = decode.get_packet_val(decode.code)
print("Ans1:", decode.version_total)
print("Ans2:", total, "Bits read:", num_bits_read)