Name:           dwf-edid
Version:        1
Release:        %autorelease
Summary:        Custom EDID for Alienware AW3423DWF containing 10bpc 165Hz and 157Hz modes.

Source:         dwf-edid-%{version}.tar.zst

License:        Apache-2.0

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

#    Copyright 2024 [Alexander Webb]

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
