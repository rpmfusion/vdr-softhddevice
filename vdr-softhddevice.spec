%global commit  37f409cb9aae06c99a6dff910b1b1d9278190ef1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20140625

Name:           vdr-softhddevice
Version:        0.6.0
Release:        16.%{gitdate}git%{shortcommit}%{?dist}
Summary:        A software and GPU emulated HD output device plugin for VDR

License:        AGPLv3
URL:            http://projects.vdr-developer.org/projects/plg-softhddevice
Source0:        http://projects.vdr-developer.org/git/vdr-plugin-softhddevice.git/snapshot/vdr-plugin-softhddevice-%{commit}.tar.bz2
# Configuration files for plugin parameters. These are Fedora specific and not in upstream.
Source1:        %{name}.conf

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

# remove .git files and Gentoo files
rm -f .indent.pro .gitignore .gitattributes
rm -f vdr-softhddevice-9999.ebuild vdr-softhddevice-9999-pre1.7.36.ebuild

for f in ChangeLog README.txt; do
  iconv -f iso8859-1 -t utf-8 $f >$f.conv
  touch -r $f $f.conv
  mv $f.conv $f
done

%build
make CFLAGS="%{optflags} -fPIC" %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
install -Dpm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/softhddevice.conf
%find_lang %{name}

%files -f %{name}.lang
%{vdr_plugindir}/libvdr-softhddevice.so.%{vdr_apiversion}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/softhddevice.conf
%doc ChangeLog README.txt AGPL-3.0.txt

%changelog
* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 0.6.0-16.20140625git37f409c
- Rebuilt for ffmpeg-2.3

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
