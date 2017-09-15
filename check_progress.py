#!/usr/bin/env python

import unittest
import boot_config as bc

def writeFile(content, path, perms=None):
    with open(path, 'w') as f:
        f.write(content)
    if perms != None:
        # TODO: add permissions setting code here.
        pass

class CheckProgress(unittest.TestCase):
    def setUp(self):
        pass

    def test_platformInfo_readWrite(self):
        content = ('VMX_LOADED=1.2.345\n'
                    + 'FOO=bar\n')
        writeFile(content, '/.platform_info')
        self.assertEqual(bc.platformInfo('FOO'), 'bar')
        self.assertEqual(bc.platformInfo('VMX_LOADED'), '1.2.345')
        bc.platformInfo('ANOTHER', 'new_content')
        self.assertEqual(bc.platformInfo('FOO'), 'bar')
        self.assertEqual(bc.platformInfo('VMX_LOADED'), '1.2.345')
        self.assertEqual(bc.platformInfo('ANOTHER'), 'new_content')

    def testgetPoolOverrides(self):
        pass

if __name__ == '__main__':
    unittest.main()

