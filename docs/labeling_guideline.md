# Labeling Guideline

## Question
Is this recall about a battery-related fire or thermal risk?

## Label 1 (positive)
- The defect is in a battery (HV traction or 12V/24V/48V) or its direct circuit/cables, AND
- the consequence mentions fire, thermal runaway, smoke, or overheating.

## Label 0 (negative)
- The battery is only mentioned as a location (e.g. a leak *near* the battery).
- Battery problem without fire risk (e.g. loss of drive power, battery drain).
- Fire risk not caused by a battery (e.g. fuel leak, engine).

## Examples
| CAMPNO | Label | Reason |
|---|---|---|
| 23V329000 | 0 | Fuel leak near HV battery cover; battery is not the cause |
| 18V553000 | 1 | 12V battery circuit can overheat and cause fire |
| 22V024000 | 0 | "Battery drainage" only; no battery fire mechanism |

## Rules
- Read only DESC_DEFECT and CONEQUENCE_DEFECT.
- Decide before looking at any keyword flags.
- If unsure, write 0 and add a note.