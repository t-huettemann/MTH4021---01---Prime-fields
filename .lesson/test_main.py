import AutoFeedback.varchecks as vc
import unittest
import rings_and_fields as r


class UnitTests(unittest.TestCase):
    def test_G(self):
        GG = r.primefield(257)
        assert(vc.check_vars('G', GG))

    def test_z(self):
        G = r.primefield(257)
        zz = G(1024)
        assert(vc.check_vars('z', zz))

    def test_y(self):
        G = r.primefield(257)
        z = G(1024)
        yy = z.power(2023)
        assert(vc.check_vars('y', yy))

    def test_b(self):
        G = r.primefield(257)
        z = G(1024)
        bb = (z.power(256) - G.one()).is_zero()
        assert(vc.check_vars('b', bb))
