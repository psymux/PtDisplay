# PtDisplay
4-20mA pressure transducer digital display project

BOM:
* TTGO 
> * https://www.aliexpress.com/item/33050667207.html?spm=a2g0o.order_list.0.0.50581802rFfEgG
* Battery
> * https://www.aliexpress.com/item/32961790770.html?spm=a2g0o.order_list.0.0.50581802rFfEgG
* Boost converter
> * https://www.aliexpress.com/item/1005002827282037.html?spm=a2g0o.order_list.0.0.50581802rFfEgG 
> * or https://www.aliexpress.com/item/1005001953396652.html?spm=a2g0o.order_list.0.0.50581802rFfEgG

Installing LoBo MicroPython on TTGO:

1. Install esptool: `pip install esptool` (https://github.com/espressif/esptool/)
2. Download LoBo firmware here: https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/firmwares
   - In this case I used the ...LoBo_ESP32_all file
3. Install the firmware 
   - You can follow this guide https://www.instructables.com/Installing-Loboris-lobo-Micropython-on-ESP32-With-/
   - But really what you need is run this command from inside the extracted directory that you downloaded from Loboris above:
     `python esptool.py --chip esp32 --port <YOUR COM PORT HERE!!!> --baud 460800 --before default_reset --after no_reset write_flash -z --flash_mode dio --flash_freq 40m --flash_size detect 0x1000 bootloader/bootloader.bin 0xf000 phy_init_data.bin 0x10000 MicroPython.bin 0x8000 partitions_mpy.bin`
     - Where `<YOUR COM PORT HERE!!!>` May be `COM3` as in my case.
4. 
