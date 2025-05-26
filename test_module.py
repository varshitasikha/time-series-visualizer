import unittest
import pandas as pd
import time_series_visualizer as tsv

class TestTimeSeriesVisualizer(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
        self.df = self.df[(self.df['value'] >= self.df['value'].quantile(0.025)) & (self.df['value'] <= self.df['value'].quantile(0.975))]

    def test_data_cleaning(self):
        # Test that data does not contain values outside quantiles
        self.assertTrue((self.df['value'] >= self.df['value'].quantile(0.025)).all())
        self.assertTrue((self.df['value'] <= self.df['value'].quantile(0.975)).all())

    def test_draw_line_plot(self):
        fig = tsv.draw_line_plot()
        self.assertIsNotNone(fig)
        # Optionally check figure properties (e.g. title)
        self.assertIn('Daily freeCodeCamp Forum Page Views', fig._suptitle.get_text() if fig._suptitle else '')

    def test_draw_bar_plot(self):
        fig = tsv.draw_bar_plot()
        self.assertIsNotNone(fig)

    def test_draw_box_plot(self):
        fig = tsv.draw_box_plot()
        self.assertIsNotNone(fig)

if __name__ == '__main__':
    unittest.main()
