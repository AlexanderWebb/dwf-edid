Name:           dwf-edid
Version:        1
Release:        %autorelease
Summary:        Custom EDID for Alienware AW3423DWF containing 10bpc 165Hz and 157Hz modes.

Source:         dwf-edid-%{version}.tar.zst

License:        MIT

%description
The factory EDID causes skipped frames when HDR with WCG is enabled in Plasma 6.
A reddit post https://www.reddit.com/r/ultrawidemasterrace/comments/10w07qb/aw3423dwf_i_successfully_managed_10bit_at_165hz/
shows that we can create a custom resolution that just barely fits under bandwidth limits by reducing pixel overscan and the
blanking interval.

This package copies the custom edid into /lib/firmware/edid/dwf_edid.bin

Intended to be used in combination with drm_kms_helper.edid_firmware kernel arg.

%prep
%setup
cp -r %{_builddir}/dwf-edid-%{version} %{_buildrootdir}/dwf-edid-%{version}-%{release}.%{_arch}

%files
/lib/firmware/edid/dwf-edid.bin
