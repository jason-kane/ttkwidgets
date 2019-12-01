button_collapse = """
#define button_collapse_width 16
#define button_collapse_height 16
static unsigned char button_collapse_bits[] = {
   0x00, 0x00, 0xfe, 0x7f, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40,
   0x02, 0x40, 0xfa, 0x5f, 0xfa, 0x5f, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40,
   0x02, 0x40, 0x02, 0x40, 0xfe, 0x7f, 0x00, 0x00 };
"""

button_collapse_mask = """
#define button_collapse_mask_width 16
#define button_collapse_mask_height 16
static unsigned char button_collapse_mask_bits[] = {
   0x00, 0x00, 0xfe, 0x7f, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40,
   0x02, 0x40, 0xfa, 0x5f, 0xfa, 0x5f, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40,
   0x02, 0x40, 0x02, 0x40, 0xfe, 0x7f, 0x00, 0x00 };
"""