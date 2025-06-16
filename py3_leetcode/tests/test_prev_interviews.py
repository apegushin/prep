import src.prev_interviews as mcd
import pytest

@pytest.mark.parametrize('curwd, cdto, result',
                        [('/', 'foo', '/foo'),
                         ('/baz', '/bar', '/bar'),
                         ('/foo/bar', '../../../../..', '/'),
                         ('/x/y', '../p/../q', '/x/q'),
                         ('/x/y', '/p/./q', '/p/q'),
                        ])
def test_cd_dir(curwd, cdto, result):
    assert mcd.cd_dir(curwd, cdto) == result