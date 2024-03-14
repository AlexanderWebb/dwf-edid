Name:           dwf_edid
Version:        1
Release:        %autorelease
Summary:        Custom EDID for Alienware AW3423DWF containing 10bpc 165Hz and 144Hz modes.

Source:         dwf_edid-%{version}.tar.zst

License:        MIT

%description
The factory EDID advertises max 10bpc in the 165Hz mode, but skips frames due to DP bandwidth limits.
A reddit post https://www.reddit.com/r/ultrawidemasterrace/comments/10w07qb/aw3423dwf_i_successfully_managed_10bit_at_165hz/
shows that we can create a custom resolution that just barely fits under bandwidth limits by reducing pixel overscan and the
blanking interval.

This package copies the custom edid into /lib/firmware/edid/dwf_edid.bin

Intended to be used in combination with drm_kms_helper.edid_firmware kernel arg.

%prep
%autosetup

%files
/usr/lib/firmware/edid/dwf_edid.bin
