import random

class Generator:
    def phone_number() -> str:
        operator_codes = {"tsel": ["811", "812", "813", "821", "822", "823", "852", "853", "851"],"isat": ["814", "815", "816", "855", "856", "857", "858", "817", "818", "819"],"xasis": ["817", "818", "819", "859", "877", "878"],"tri": ["895", "896", "897", "898", "899"],"smartf": ["881", "882", "883", "884", "885", "886", "887", "888", "889"],"axis": ["838", "831", "832", "833"]}
        nomor_pelanggan = random.randrange(000000, 999999)
        return '+62'+ random.choice(operator_codes[random.choice(['tsel','isat','xasis','tri','smartf', 'axis'])]) + str(nomor_pelanggan)

    def name() -> tuple:
        data = random.choice([{'type': '1', 'name': ['Aurel', 'Siti', 'Annita', 'Risma', 'Salwa', 'Nadin', 'Putri', 'Viola', 'Fitri', 'Zahra', 'Sarah', 'Anna', 'Vina', 'Laila', 'Amelia']}, {'type': '2', 'name': ['Ahmad', 'Adrian', 'Andre', 'Alif', 'Dean', 'Dimas', 'Desta', 'Fauzan', 'Ivan', 'Fendik', 'Brodin', 'Wawan', 'Salim', 'Nor', 'Afif', 'Muhammad', 'Azzam', 'Putra', 'Pegi', 'Setiawan']}])
        name = random.choice(data['name']) +' '+ random.choice(data['name'])
        return (data['type'], name)

    def ttl() -> tuple:
        day = random.randrange(1, 28)
        month = random.randrange(1, 12)
        year = random.randrange(1985, 2004)
        return (day, month, year)
