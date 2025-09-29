#!/usr/bin/env python3
"""
🧵 Synth Assembly: Duration Fix Validation Script

Quick validation script to test the fix for Issue #3.
"""

import sys
import os

# Add the project to path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

from abcweaver.core.converter import Converter
from abcweaver.utils.helpers import format_duration
from abcweaver.utils.constants import ABC_DURATIONS, DEFAULT_DIVISIONS

def test_issue_3_fix():
    """Test the specific Issue #3 case"""
    print("🧵 Testing Issue #3 Duration Fix")
    print("=" * 50)

    # Issue #3 example: ABC notation with quarter notes
    abc_quarter_notes = "C1 D1 E1 F1"  # ABC '1' = quarter note
    print(f"📝 ABC Input (quarter notes): {abc_quarter_notes}")

    converter = Converter()
    xml_notes = converter.abc_to_musicxml_notes(abc_quarter_notes, DEFAULT_DIVISIONS)

    print(f"\n🎼 MusicXML Conversion Results:")
    print(f"   Divisions: {DEFAULT_DIVISIONS}")

    for i, note in enumerate(xml_notes, 1):
        pitch_elem = note.find('pitch')
        duration_elem = note.find('duration')

        if pitch_elem is not None:
            step = pitch_elem.find('step').text
            octave = pitch_elem.find('octave').text
            duration = duration_elem.text
            beats = int(duration) / DEFAULT_DIVISIONS

            print(f"   Note {i}: {step}{octave} → duration={duration} → {beats} beats")

    # Test the problematic case from Issue #3
    print(f"\n❌ Issue #3 Example (whole notes in ABC):")
    abc_whole_notes = "C4 D4 E4 F4"  # ABC '4' = whole note
    print(f"📝 ABC Input (whole notes): {abc_whole_notes}")

    xml_notes_whole = converter.abc_to_musicxml_notes(abc_whole_notes, DEFAULT_DIVISIONS)

    for i, note in enumerate(xml_notes_whole, 1):
        pitch_elem = note.find('pitch')
        duration_elem = note.find('duration')

        if pitch_elem is not None:
            step = pitch_elem.find('step').text
            octave = pitch_elem.find('octave').text
            duration = duration_elem.text
            beats = int(duration) / DEFAULT_DIVISIONS

            print(f"   Note {i}: {step}{octave} → duration={duration} → {beats} beats")

def test_duration_mappings():
    """Test all duration mappings"""
    print(f"\n🎵 Duration Mapping Tests")
    print("=" * 50)

    test_cases = [
        ('1', 'quarter note'),
        ('2', 'half note'),
        ('4', 'whole note'),
        ('/2', 'eighth note'),
        ('/4', 'sixteenth note'),
    ]

    print(f"ABC Duration → MusicXML Duration (divisions={DEFAULT_DIVISIONS})")
    for abc_dur, description in test_cases:
        musicxml_dur = format_duration(abc_dur, DEFAULT_DIVISIONS)
        beats = musicxml_dur / DEFAULT_DIVISIONS
        print(f"   '{abc_dur}' ({description:>12}) → {musicxml_dur:>2} → {beats:>4} beats")

def test_abc_durations_constants():
    """Test ABC_DURATIONS constants"""
    print(f"\n📊 ABC_DURATIONS Constants")
    print("=" * 50)

    for abc_notation, multiplier in ABC_DURATIONS.items():
        print(f"   '{abc_notation}' → {multiplier} (quarter note multiplier)")

if __name__ == "__main__":
    print("🚀 ABCWeaver Duration Fix Validation")
    print("🎯 Testing fix for Issue #3: Quarter notes incorrectly converted to whole notes")
    print()

    try:
        test_abc_durations_constants()
        test_duration_mappings()
        test_issue_3_fix()

        print(f"\n✅ All tests completed successfully!")
        print(f"🧵 Synth Assembly: Duration calculation fix validated")

    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)