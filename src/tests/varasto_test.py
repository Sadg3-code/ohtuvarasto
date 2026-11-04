import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    def test_tilavuus_nolla_nollataan(self):
        self.assertAlmostEqual(Varasto(0).tilavuus, 0)
    
    def test_alku_saldo_negatiivinen(self):
        self.assertAlmostEqual(Varasto(10, -1).saldo, 0)

    def test_saldo_suurempi_kuin_tilavuus(self):
        self.assertAlmostEqual(Varasto(10, 15).saldo, 10)

    def test_varastoon_lisataa_negatiivnen_luku(self):
        self.varasto.lisaa_varastoon(-3)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisataan_enemman_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_ottaminen_palauttaa_nollan(self):
        self.varasto.lisaa_varastoon(5)

        self.assertAlmostEqual(self.varasto.ota_varastosta(-2), 0)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_maara_on_suurempi_kuin_saldo(self):
        self.varasto.lisaa_varastoon(10)

        self.assertAlmostEqual(self.varasto.ota_varastosta(15), 10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_paljonko_mahtuu(self):
        v = Varasto(10.0)
        v.lisaa_varastoon(4.0)
        self.assertEqual(str(v), "saldo = 4.0, vielä tilaa 6.0")