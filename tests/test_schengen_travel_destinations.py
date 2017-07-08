from labyrinth_test_case import LabyrinthTestCase
from lwotai import Labyrinth, Randomizer
from mockito import when, mock


class TravelDestinationsForSchengenVisasTest(LabyrinthTestCase):

    def test_us_hard_and_one_unmarked_schengen(self):
        # Set up
        app = Labyrinth(1, 1, self.set_up_test_scenario)
        app.map["United States"].posture = "Hard"
        schengen_countries = self.schengen_countries(app)
        for schengen_country in schengen_countries[1:]:
            schengen_country.posture = "Anything"
        unmarked_country = schengen_countries[0]
        unmarked_country.posture = ""

        # Invoke
        destinations = app.travelDestinationsSchengenVisas()

        # Check
        expected_country = unmarked_country.name
        self.assertEqual(destinations, [expected_country, expected_country])

    def test_us_hard_and_multiple_unmarked_schengens(self):
        # Set up
        mock_randomizer = mock(Randomizer())
        app = Labyrinth(1, 1, self.set_up_test_scenario, randomizer=mock_randomizer)
        schengen_countries = self.schengen_countries(app)
        schengen_country_names = [country.name for country in schengen_countries]
        chosen_countries = ['c1', 'c2']
        when(mock_randomizer).pick(2, schengen_country_names).thenReturn(chosen_countries)
        app.map["United States"].posture = "Hard"
        for country in schengen_countries:
            country.posture = ""

        # Invoke
        destinations = app.travelDestinationsSchengenVisas()

        # Check
        self.assertEqual(destinations, chosen_countries)