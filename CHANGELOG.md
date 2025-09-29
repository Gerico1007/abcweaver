# Changelog

All notable changes to ABCWeaver will be documented in this file.

## [0.2.1] - 2024-09-28

### 🐛 Bug Fixes
- **Critical Fix**: Resolved Issue #3 - Quarter notes incorrectly converted to whole notes
- Fixed ABC duration mapping in constants to follow standard ABC notation
- Corrected format_duration logic to properly handle quarter note as base unit
- Fixed reverse conversion from MusicXML to ABC duration strings
- Improved ABC parser regex pattern to correctly parse fractional durations (`/2`, `/4`, etc.)

### ✅ Testing
- Added comprehensive test suite with 11 test cases for duration calculations
- Added bidirectional conversion accuracy validation
- Added regression tests specifically for Issue #3
- Created validation script for duration fix verification

### 📚 Documentation
- Updated PyPI publication guide with new version information
- Added detailed changelog with version history

### 🔧 Technical Details
**Root Cause**: ABC notation interpretation was incorrect throughout the codebase:
- Fixed: ABC `'1'` now correctly represents quarter note (base unit)
- Fixed: ABC `'2'` now correctly represents half note (2 beats)
- Fixed: ABC `'4'` now correctly represents whole note (4 beats)
- Fixed: ABC `'/2'` now correctly represents eighth note (0.5 beats)

**Impact**: This fix ensures accurate musical timing in all ABC ↔ MusicXML conversions.

## [0.2.0] - 2024-08-19

### 🎼 Initial Release
- ABC ↔ MusicXML bidirectional conversion engine
- Redis stream processing integration
- Command-line interface
- Core parsing and conversion functionality
- Basic validation and error handling

---

**♠️🌿🎸🤖🧵 G.Music Assembly Development Record**