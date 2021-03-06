import random
from unittest.mock import patch

from nose.tools import eq_

from pyecharts import options as opts
from pyecharts.charts import Polar


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_polar_scatter(fake_writer):
    data = [(i, random.randint(1, 100)) for i in range(101)]
    c = Polar().add("", data, type_="scatter", label_opts=opts.LabelOpts(is_show=False))
    c.render()
    _, content = fake_writer.call_args[0]
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")
