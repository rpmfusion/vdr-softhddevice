# version we want build against
%global vdr_version 2.6.1
%if 0%{?fedora} >= 38
%global vdr_version 2.6.3
%endif

Name:           vdr-softhddevice
Version:        1.10.0
Release:        1%{?dist}
Summary:        A software and GPU emulated HD output device plugin for VDR

License:        AGPLv3
URL:            https://github.com/ua0lnj/vdr-plugin-softhddevice
Source0:        %url/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Configuration files for plugin parameters. These are Fedora specific and not in upstream.
Source1:        %{name}.conf

BuildRequires:  gcc-c++
BuildRequires:  vdr-devel >= %{vdr_version}
BuildRequires:  gettext
BuildRequires:  libva-devel
BuildRequires:  libvdpau-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  ffmpeg
BuildRequires:  ffmpeg-devel
BuildRequires:  glm-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mesa-libGL-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
Requires:       xorg-x11-server-Xorg

%description
A software and GPU emulated UHD output device plugin for VDR.

    Video decoder CPU / VA-API / VDPAU / CUVID
    Video output VA-API / VDPAU / GLX (VA-API / CUVID)
    OSD accelerated by GPU VDPAU / CUVID
    Audio FFMpeg / Alsa / Analog
    Audio FFMpeg / Alsa / Digital
    Audio FFMpeg / OSS / Analog
    HDMI/SPDIF pass-through
    Software volume, compression, normalize and channel resample
    VDR ScaleVideo API
    Software deinterlacer Bob (VA-API only)
    Autocrop
    Grab image (VA-API / VDPAU / CUVID)
    Suspend / Dettach
    Letterbox, Stretch and Center cut-out video display modes
    atmo light support with plugin http://github.com/durchflieger/DFAtmo
    PIP (Picture-in-Picture) (VDPAU / CUVID)

    planned: OSD accelerated by GPU VA-API
    planned: Video output Opengl / Xv
    planned: Improved software deinterlacer (yadif or/and ffmpeg filters)
    XvBa support is no longer planned (use future Radeon UVD VDPAU)

%prep
%autosetup -p1 -n vdr-plugin-softhddevice-%{version}

# remove .git files and Gentoo files
rm -f .indent.pro .gitignore .gitattributes
rm -f vdr-softhddevice-9999.ebuild vdr-softhddevice-9999-pre1.7.36.ebuild

for f in ChangeLog README.txt; do
  iconv -f iso8859-1 -t utf-8 $f >$f.conv
  touch -r $f $f.conv
  mv $f.conv $f
done

%build
%make_build CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC"

%install
%make_install
install -Dpm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/softhddevice.conf
%find_lang %{name}

%files -f %{name}.lang
%{vdr_plugindir}/libvdr-softhddevice.so.%{vdr_apiversion}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/softhddevice.conf
%doc ChangeLog README.txt
%license AGPL-3.0.txt

%changelog
* Tue Mar 21 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.10.0-1
- Update to 1.10.0

* Mon Mar 06 2023 Leigh Scott <leigh123linux@gmail.com> - 1.9.7-2
- Rebuild for new ffmpeg

* Thu Dec 22 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.9.7-1
- Update to 1.9.7

* Sun Dec 18 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.8.2-4
- Rebuilt for new VDR API version

* Sat Dec 03 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.8.2-3
- Rebuilt for new VDR API version

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Mon Jul 18 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.8.2-1
- Update to 1.8.2

* Fri Apr 22 2022 Sérgio Basto <sergio@serjux.com> - 1.4.0-2
- set minimum version of vdr for each branch

* Thu Apr 21 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0

* Mon Apr 11 2022 Sérgio Basto <sergio@serjux.com> - 1.2.8-2
- Rebuilt for VDR 2.6.1

* Fri Feb 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.8-1
- Update to 1.2.8

* Sat Jan 08 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.7-1
- Update to 1.2.7

* Thu Dec 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.2.5-2
- Rebuilt for new VDR API version

* Mon Nov 29 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.2.5-1
- Update to 1.2.5

* Sat Nov 06 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.2.4-1
- Update to 1.2.4

* Sat Jul 31 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.2.2-1
- Update to 1.2.2

* Fri Jul 09 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Sat Jun 19 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Mon May 31 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1

* Mon Apr 26 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.1.0-2
- Rebuilt for new VDR API version

* Mon Apr 05 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Tue Mar 23 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.15-1
- Update to 1.0.15
- Add BR glm-devel

* Sat Feb 27 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.14-1
- Update to 1.0.14

* Fri Feb 12 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.13-1
- Update to 1.0.13

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.12-1
- Update to 1.0.12

* Tue Jan 05 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.11-1
- Update to 1.0.11

* Mon Jan 04 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.10-1
- Update to 1.0.10

* Mon Jan 04 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.9-2
- Rebuilt for new VDR API version

* Tue Dec 29 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.0.9-1
- Use fork because its under maintenance
- fixes (rfbz#5882)

* Wed Oct 21 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-27.20151103git6dfa88a
- Rebuilt for new VDR API version

* Thu Aug 27 2020 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-26.20151103git6dfa88a
- Rebuilt for new VDR API version

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.1-25.20151103git6dfa88a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.1-24.20151103git6dfa88a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.1-23.20151103git6dfa88a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-22.20151103git6dfa88a
- Rebuilt for new VDR API version 2.4.1

* Sun Jun 30 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-21.20151103git6dfa88a
- Rebuilt for new VDR API version

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-20.20151103git6dfa88a
- Rebuilt for new VDR API version

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.1-19.20151103git6dfa88a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-18.20151103git6dfa88a
- Add BR gcc-c++

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.6.1-17.20151103git6dfa88a
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.6.1-16.20151103git6dfa88a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-15.20151103git6dfa88a
- Rebuilt for vdr-2.4.0

* Mon Feb 26 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.6.1-14.20151103git6dfa88a
- Use compat-ffmpeg28 for F28

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.6.1-13.20151103git6dfa88a
- Rebuilt for ffmpeg-3.5 git

* Mon Jan 15 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.6.1-12.20151103git6dfa88a
- Rebuilt for VA-API 1.0.0

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.6.1-11.20151103git6dfa88a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 30 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.6.1-10.20151103git6dfa88a
- Rebuild for ffmpeg update

* Tue Jun 28 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-9.20151103git6dfa88a
- Added ffmpeg_2.9.patch

* Wed Nov 04 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-8.20151103git6dfa88a
- update for new git snapshot

* Wed Oct 07 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-7.20151006gitee2311d
- update for new git snapshot

* Fri Oct 02 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-6.20151001git5dc5601
- update for new git snapshot

* Wed Sep 30 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-5.20150930gitf47ee3a
- update for new git snapshot

* Fri Sep 25 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-4.20150924git509329c
- update for new git snapshot

* Wed Aug 26 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-3.20150826git8c347fd
- update for new git snapshot

* Mon Aug 17 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-2.20150817git06b8f77
- update for new git snapshot

* Fri Aug 14 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.1-1.20150810git700c8e8
- update for new git snapshot

* Sat Jul 04 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-30.20150630gitec58e45
- renamed arm.patch to chartype.patch

* Tue Jun 30 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-29.20150630gitec58e45
- update for new git snapshot

* Mon Jun 29 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-28.20150619git396d5fa
- added R xorg-x11-server-Xorg
- added exit-crash.patch
- added arm.patch

* Fri Jun 19 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-27.20150619git396d5fa
- update for new git snapshot

* Wed Apr 22 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-26.20150422gitf0d31ad
- update for new git snapshot

* Tue Mar 10 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-25.20150310gita1939eb
- update for new git snapshot

* Mon Feb 16 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-24.20150216git93ea660
- update for new git snapshot

* Thu Feb 12 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-23.20150212git1d06c5b
- update for new git snapshot
- Compile with vdr 2.1.10
- mark license files as %%license where available

* Mon Feb 09 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-22.20150209git2ceeb6d
- update for new git snapshot

* Mon Oct 20 2014 Sérgio Basto <sergio@serjux.com> - 0.6.0-21.20141016git9f134c1
- Rebuilt for FFmpeg 2.4.3

* Thu Oct 16 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-20.20141016git9f134c1
- update for new git snapshot

* Wed Oct 15 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-19.20141013gitac1d525
- update for new git snapshot

* Sat Oct 11 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-18.20141011gitc2556eb
- update for new git snapshot

* Wed Sep 24 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-17.20140924gita3c0052
- update for new git snapshot

* Wed Aug 13 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-16.20140813git8b7402a
- update for new git snapshot

* Wed Jun 25 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-15.20140625git37f409c
- update for new git snapshot

* Wed Jun 04 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-14.20140604git5207af6
- update for new git snapshot

* Sun Apr 20 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-13.20140420git0cdedb8
- changed Summary
- update for new git snapshot

* Fri Feb 28 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-12.20140228git42bbb76
- update for new git snapshot

* Thu Feb 13 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-11.20140212git3d3a88e
- update for new git snapshot

* Wed Jan 29 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-10.20140129git340e10a
- update for new git snapshot

* Fri Jan 24 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-9.20140124gita45b9a3
- update for new git snapshot
- added gitdate

* Tue Jan 14 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-8.590bae4
- update for new git snapshot

* Thu Jan 09 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-7.978fc59
- removed gittag
- updated description
- put together README and changelog file conversion in %%prep section
- removed sed patching of Makefile
- changed changelog revision
- changed build flags

* Thu Jan 09 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-6.git978fc59
- used macro commit in Source
- cleanup %%install section
- removed marcro defattr
- removed marcro pname
- removed marcro commitdate

* Wed Jan 08 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-5.20140108git978fc59
- update for new git snapshot

* Mon Jan 06 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-4.20131204git8577292
- update for new git snapshot

* Mon Jan 06 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-3.20131204gita74a8e1
- correct git snapshot address 
- correct wrong git date in %%changelog

* Sun Jan 05 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-2.20131204gita74a8e1
- rebuild
- changed license type
- correct url address
- removed .git files

* Sun Dec 22 2013 Martin Gansser <martinkg@fedoraproject.org> - 0.6.0-1.20131204gita74a8e1
- rebuild for new version

* Sat Dec 31 2011 Zoran Pericic <zpericic@netst.org> - 0.1.4-1
- Initial build
