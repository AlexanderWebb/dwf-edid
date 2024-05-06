# Custom EDID for ALienware AW3423DWF

## Why use a custom EDID

The Dell Alienware AW3423DWF (referred to as dwf) only broadcasts support for 165 hz, 100 hz, and 60 hz at 3440x1440 resolution.

Despite supporting 165hz refresh rate, HDR, and 10-bit color individually, the monitor cannot do all of these at once using the stock firmware timings.
This is because the bandwidth is greater than what the HBR3 DisplayPort standard supports. Trying to do so anyway results in frame skipping.

## Installation

### Fedora Linux

There's a COPR with instructions for Fedora Atomic desktops at https://copr.fedorainfracloud.org/coprs/atwebb/dwf-edid/

### Other Linux Distros

1. Extract dwf-edid.bin from tar file
2. Move dwf-edid.bin to the /usr/lib/firmware/edid/ directory. (This directory is special to the kernel. AFAIK others don't work at all.)
3. Add /usr/lib/firmware/edid/dwf-edid.bin to initramfs.
4. Add `drm.edid_firmware=edid/dwf-edid.bin` to kernel args.
5. Reboot. If it didn't work, the kernel *should* fall back to the monitor's edid.

### Windows/Mac

1. Extract dwf-edid.bin from tar file (7-Zip probably works)
2. Try following that reddit thread? No experience here.

## Build

### Dependencies
`dnf install fedpkg`

### Build SRPM and RPM
`fedpkg mockbuild`

## On monitor timings

The industry standards for monitor timings were originally designed for CRT TVs. They had to mechanically move the electron gun. Displays used "blanking intervals" where the analog signal was "blank" for a certain period of time to allow the CRT to move to the next line. This was standardized as CVT timing. Modern LCD displays still use this interval as time to process the signal.

There's various "reduced" standards since we don't use electron guns anymore, and the timing can be further reduced through trial and error. The most recent is CVT-RBv2.

Other components may use the blanking time based on a [forum post](https://www.monitortests.com/forum/Thread-Why-do-LCD-displays-need-blank-intervals) by ToastyX (who wrote CRU)

>It's mostly a holdover from the CRT days, but digital monitors still need time to process the signal. Many LCD monitors can't handle very low blanking intervals. I find with most monitors, the total blanking matters more than the individual porch/sync parameters.
>
>Blanking also has other uses. HDMI uses the blanking periods to transmit audio and other data. Video cards use the vertical blanking time to retrain the memory when changing clock speeds so it doesn't corrupt the screen contents. FreeSync uses the vertical blanking time to delay the next refresh until a frame is ready.

You can view various timings compared to bandwidth at https://tomverbeure.github.io/video_timings_calculator. Note that DisplayPort Stream Compression (DSC) is not implemented on this monitor.

## Included dwf monitor timings

The 157 hz option is based on [this reddit post](https://www.reddit.com/r/ultrawidemasterrace/comments/yyaj82/aw3423dwf_can_do_10bit_hdr_150hz_frequency/) by /u/chlronald.

The most modern CVT standard is CVT-RBv2, and 157hz at those timings uses 99% of HBR3 bandwidth.

The 165 hz option is based on [a different reddit post](https://www.reddit.com/r/ultrawidemasterrace/comments/10w07qb/aw3423dwf_i_successfully_managed_10bit_at_165hz/) by /u/iyesgames.

The 165 hz timings are non-standard, and use around 97% of HBR3 bandwidth. If you have weird graphics artifacts, try the 157 hz option instead.

## License

The EDID itself is not copyrightable. It's a list of the monitor's technical specifications in binary form, and a list of facts cannot be copyrighted. See https://www.copyright.gov/circs/circ33.pdf

The rest of the files are available under Apache-2.0. Because I don't want to have to wrangle with adding a license file to the `%files` section.

   Copyright [2024] [Alexander Webb]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
