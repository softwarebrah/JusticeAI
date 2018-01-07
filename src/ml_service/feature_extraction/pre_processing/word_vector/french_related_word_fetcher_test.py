import unittest
from bs4 import BeautifulSoup
from feature_extraction.pre_processing.word_vector.french_related_word_fetcher import _find_plural, _find_fem_plural, \
    _find_feminin, _find_conjugation, _find_synonym


class TestRelatedWordFetcher(unittest.TestCase):

    def test_find_feminin(self):
        # Test Data
        data = """
            <p>
              <b>locatrice</b>
              <a href="/wiki/Annexe:Prononciation/fran%C3%A7ais" title="Annexe:Prononciation/français">
                <span class="API" title="prononciation API">\lɔ.ka.tʁis\</span>
              </a>
            </p>
            <ol>
              <li><i>Féminin de</i> <a href="/wiki/locateur#fr" title="locateur">locateur</a>.</li>
            </ol>
        """
        soup = BeautifulSoup(data, "html.parser")

        # Execute
        result = _find_feminin(soup)

        # Verify
        self.assertEqual(result, "locateur")

    def test_find_plural(self):
        # Test Data
        data = """
            <p>
              <b>locateurs</b> <a href="/wiki/Annexe:Prononciation/fran%C3%A7ais" title="Annexe:Prononciation/français">
                <span class="API" title="prononciation API">\lɔ.ka.tœʁ\</span>
              </a> <span class="ligne-de-forme">
              <i>masculin</i>
            </span>
            </p>
            <ol>
            <li>
              <i>Pluriel de</i> <a href="/wiki/locateur#fr" title="locateur">locateur</a>.</li>
            </ol>
        """
        soup = BeautifulSoup(data, "html.parser")

        # Execute
        result = _find_plural(soup)

        # Verify
        self.assertEqual(result, "locateur")

    def test_find_fem_plural(self):
        # Test Data
        data = """
            <p>
              <b>locatrices</b> <a href="/wiki/Annexe:Prononciation/fran%C3%A7ais" title="Annexe:Prononciation/français">
                <span class="API" title="prononciation API">\lɔ.ka.tʁis\</span>
              </a>
            </p>
            <ol>
              <li>
                <i>Féminin pluriel de</i> <a href="/wiki/locateur#fr" title="locateur">locateur</a>.
              </li>
            </ol>
        """
        soup = BeautifulSoup(data, "html.parser")

        # Execute
        result = _find_fem_plural(soup)

        # Verify
        self.assertEqual(result, "locateur")

    def test_find_synonym(self):
        # Test Data
        data = """
            <h4>
            <span class="mw-headline" id="Synonymes">
              <span class="">Synonymes</span>
            </span>
            <span class="mw-editsection">
              <span class="mw-editsection-bracket">[</span>
              <a href="/w/index.php?title=locateur&amp;action=edit&amp;section=4" title="Modifier la section : Synonymes">modifier</a>
              <span class="mw-editsection-bracket">]</span>
            </span>
            </h4>
            <ul>
              <li>
                <a href="/wiki/loueur" title="loueur">loueur</a>
              </li>
              <li>
                <a href="/wiki/bailleur" title="bailleur">bailleur</a>
              </li>
            </ul>
        """
        soup = BeautifulSoup(data, "html.parser")

        # Execute
        result = _find_synonym(soup)

        # Verify
        self.assertEqual(result, "loueur")

    def test_find_conjugation(self):
        # Test Data
        data = """
            <table class="flextable">
              <tbody>
                <tr>
                  <th colspan="3">
                    <small>
                    <a href="/wiki/Annexe:Conjugaison_en_fran%C3%A7ais/louer" title="Annexe:Conjugaison en français/louer">Conjugaison du verbe <i>louer</i>
                    </a>
                    </small>
                  </th>
                </tr>
              </tbody>
            </table>
        """
        soup = BeautifulSoup(data, "html.parser")

        # Execute
        result = _find_conjugation(soup)

        # Verify
        self.assertEqual(result, "louer")