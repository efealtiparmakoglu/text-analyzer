#!/usr/bin/env python3
"""
Text Analyzer - Basit Metin Analiz Araci
@author: efealtiparmakoglu
@date: 2026-03-19
"""

import re
from collections import Counter
from typing import Dict, List, Tuple


class TextAnalyzer:
    """Metin analizi yapmak icin kullanilan sinif"""
    
    def __init__(self, text: str):
        self.text = text
        self.words = self._extract_words()
    
    def _extract_words(self) -> List[str]:
        """Metinden kelimeleri cikarir"""
        return re.findall(r'\b[a-zA-Z]+\b', self.text.lower())
    
    def word_count(self) -> int:
        """Toplam kelime sayisini dondurur"""
        return len(self.words)
    
    def char_count(self, include_spaces: bool = True) -> int:
        """Karakter sayisini dondurur"""
        if include_spaces:
            return len(self.text)
        return len(self.text.replace(' ', ''))
    
    def sentence_count(self) -> int:
        """Cumle sayisini dondurur"""
        sentences = re.split(r'[.!?]+', self.text)
        return len([s for s in sentences if s.strip()])
    
    def most_common_words(self, n: int = 5) -> List[Tuple[str, int]]:
        """En sik kullanilan kelimeleri dondurur"""
        return Counter(self.words).most_common(n)
    
    def average_word_length(self) -> float:
        """Ortalama kelime uzunlugunu dondurur"""
        if not self.words:
            return 0.0
        return sum(len(word) for word in self.words) / len(self.words)
    
    def analyze(self) -> Dict:
        """Tam analiz raporu olusturur"""
        return {
            'word_count': self.word_count(),
            'char_count_with_spaces': self.char_count(True),
            'char_count_without_spaces': self.char_count(False),
            'sentence_count': self.sentence_count(),
            'average_word_length': round(self.average_word_length(), 2),
            'most_common_words': self.most_common_words(5)
        }


def main():
    """Ornek kullanim"""
    sample_text = """
    Python, nesne yonelimli, yorumlamali, birlestirici ve etkilesimli 
    yuksek seviyeli bir programlama dilidir. Modulerligi ve okunabilirligi 
    ile one cikar. Python, ozellikle yapay zeka ve veri bilimi alanlarinda 
    yaygin olarak kullanilir.
    """
    
    analyzer = TextAnalyzer(sample_text)
    results = analyzer.analyze()
    
    print("=" * 50)
    print("METIN ANALIZ RAPORU")
    print("=" * 50)
    print(f"Kelime Sayisi: {results['word_count']}")
    print(f"Karakter Sayisi (bosluklu): {results['char_count_with_spaces']}")
    print(f"Karakter Sayisi (bosluksuz): {results['char_count_without_spaces']}")
    print(f"Cumle Sayisi: {results['sentence_count']}")
    print(f"Ortalama Kelime Uzunlugu: {results['average_word_length']}")
    print("\nEn Sik Kullanilan Kelimeler:")
    for word, count in results['most_common_words']:
        print(f"  - {word}: {count} kez")
    print("=" * 50)


if __name__ == "__main__":
    main()
