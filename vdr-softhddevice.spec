%global commit 	5dc5601576c617516ec41c9c4899d3e18c0cc030
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20151001

Name:           vdr-softhddevice
Version:        0.6.1
Release:        6.%{gitdate}git%{shortcommit}%{?dist}
Summary:        A software and GPU emulated HD output device plugin for VDR

License:        AGPLv3
URL:            http://projects.vdr-developer.org/projects/plg-softhddevice
Source0:        http://projects.vdr-developer.org/git/vdr-plugin-softhddevice.git/snapshot/vdr-plugin-softhddevice-%{commit}.tar.bz2
# Configuration files for plugin parameters. These are Fedora specific and not in upstream.
Source1:        %{name}.conf
# http://projects.vdr-developer.org/issues/1417
Patch0:         exit-crash.patch
# http://projects.vdr-developer.org/issues/1916
Patch1:         chartype.patch

BuildRequires:  vdr-devel >= 1.7.22
BuildRequires:  gettext
BuildRequires:  libva-devel
BuildRequires:  libvdpau-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mesa-libGL-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
Requires:       xorg-x11-server-Xorg

%description
A software and GPU emulated HD output device plugin for VDR.

    Video decoder CPU / VDPAU
    Video output VDPAU
    Audio FFMpeg / Alsa / Analog
    Audio FFMpeg / Alsa / Digital
    Audio FFMpeg / OSS / Analog
    HDMI/SPDIF pass-through
    Software volume, compression, normalize and channel resample
    VDR ScaleVideo API
    Software deinterlacer Bob (VA-API only)
    Autocrop
    Grab image (VDPAU only)
    Suspend / Dettach
    Letterbox, Stretch and Center cut-out video display modes
    atmo light support with plugin http://github.com/durchflieger/DFAtmo
    PIP (Picture-in-Picture) (VDPAU only)


%prep
%setup -qn vdr-plugin-softhddevice-%{commit}
%patch0 -p1
%patch1 -p0

# remove .git files and Gentoo files
rm -f .indent.pro .gitignore .gitattributes
rm -f vdr-softhddevice-9999.ebuild vdr-softhddevice-9999-pre1.7.36.ebuild

for f in ChangeLog README.txt; do
  iconv -f iso8859-1 -t utf-8 $f >$f.conv
  touch -r $f $f.conv
  mv $f.conv $f
done

%build
make CFLAGS="%{optflags} -fPIC" CXXFLAGS="%{optflags} -fPIC" %{?_smp_mflags}

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
