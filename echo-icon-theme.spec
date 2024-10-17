%define git_head cc6da5b
%define checkout 20081003
%define alphatag %{checkout}git%{git_head}

Name:		echo-icon-theme
Version:	0.3.89.0
Release:	0.11.%{alphatag}.4
Summary:	Echo icon theme

Group:		Graphical desktop/Other
License:	CC-BY-SA
URL:		https://fedoraproject.org/wiki/Artwork/EchoDevelopment
Source0:	%{name}-%{version}.tar.bz2
Patch0:		echo-icon-theme-0.3.89.0-icon-naming.patch
BuildArch:	noarch
Requires(post):	gtk2 >= 2.6.0
Requires(postun):	gtk2 >= 2.6.0
BuildRequires:	icon-naming-utils >= 0.8.7
BuildRequires:	perl(XML::SAX)
Requires:	gnome-icon-theme

#for Clearlooks icon theme dependency
Requires:	gnome-themes

%description
This package contains the Echo icon theme from Fedora.


%prep
%setup -q -n %{name}-%version
%patch0 -p1 -b .icon-naming

%{_bindir}/autoreconf --install

%build
%configure2_5x
%make

%install
%makeinstall_std
touch %{buildroot}%{_datadir}/icons/Echo/icon-theme.cache

%post
%update_icon_cache Echo

%postun
%clean_icon_cache Echo

%files
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING
%dir %{_datadir}/icons/Echo
%{_datadir}/icons/Echo/index.theme
%_datadir/icons/Echo/??x??/
%_datadir/icons/Echo/???x???/
%_datadir/icons/Echo/scalable
%ghost %_datadir/icons/Echo/icon-theme.cache




%changelog
* Mon Sep 12 2011 Götz Waschk <waschk@mandriva.org> 0.3.89.0-0.11.20081003gitcc6da5b.3mdv2012.0
+ Revision: 699464
- fix build

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.3.89.0-0.11.20081003gitcc6da5b.2mdv2011.0
+ Revision: 437225
- rebuild

* Wed Oct 15 2008 Götz Waschk <waschk@mandriva.org> 0.3.89.0-0.11.20081003gitcc6da5b.1mdv2009.1
+ Revision: 293962
- new snapshot
- update patch

* Mon Sep 08 2008 Götz Waschk <waschk@mandriva.org> 0.3.89.0-0.8.20080828git3e5f61d.1mdv2009.0
+ Revision: 282484
- new snapshot from Fedora

* Fri Aug 15 2008 Götz Waschk <waschk@mandriva.org> 0.3.89.0-0.8.20080803git1c213a2.1mdv2009.0
+ Revision: 272218
- new snapshot from fedora
- update the patch

* Thu Jul 10 2008 Götz Waschk <waschk@mandriva.org> 0.3.89.0-0.7.git1f550b3.2mdv2009.0
+ Revision: 233449
- rebuild for fixed rpm-mandriva-setup-build

* Thu Jul 10 2008 Götz Waschk <waschk@mandriva.org> 0.3.89.0-0.7.git1f550b3.1mdv2009.0
+ Revision: 233344
- new version from Fedora
- update license
- fix build with new icon-naming-utils
- update file list
- add missing make call

* Tue Jun 10 2008 Götz Waschk <waschk@mandriva.org> 0.3.89.0-0.git51c57605.1mdv2009.0
+ Revision: 217478
- new snapshot from Fedora
- fix build
- fix file list

* Mon Jan 14 2008 Götz Waschk <waschk@mandriva.org> 0.3.1-1mdv2008.1
+ Revision: 151267
- new version
- depend on gnome-themes and gnome-icon-theme

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 22 2007 Götz Waschk <waschk@mandriva.org> 0.3-0.git.1mdv2008.1
+ Revision: 101088
- new version
- drop patch
- sync with Fedora

* Tue Aug 28 2007 Götz Waschk <waschk@mandriva.org> 0.2-0.20070427wiki.1mdv2008.0
+ Revision: 72561
- new version
- patch to fix context in index.theme

* Fri May 04 2007 Götz Waschk <waschk@mandriva.org> 0.2-0.20070419wiki.1mdv2008.0
+ Revision: 22307
- new version


* Wed Mar 14 2007 Götz Waschk <waschk@mandriva.org> 0.2-0.20070314wiki.1mdv2007.1
+ Revision: 143369
- new snapshot

* Fri Mar 02 2007 Götz Waschk <waschk@mandriva.org> 0.2-0.20070302wiki.1mdv2007.1
+ Revision: 131059
- new checkout

* Fri Mar 02 2007 Götz Waschk <waschk@mandriva.org> 0.2-0.20070206wiki.1mdv2007.1
+ Revision: 130966
- Import echo-icon-theme

* Fri Mar 02 2007 Götz Waschk <waschk@mandriva.org> 0.2-0.20070206wiki.1mdv2007.1
- adapt for Mandriva

* Tue Feb 06 2007 Matthias Clasen <mclasen@redhat.com> - 0.2-1.20070206wiki
- New snapshot

* Mon Feb 05 2007 Matthias Clasen <mclasen@redhat.com> - 0.1-7
- Neuter macros in %%changelog

* Fri Oct 27 2006 David Zeuthen <davidz@redhat.com> - 0.1-6
- Make this package own %%{_datadir}/icons/Echo
- Preserve timestamps
- Keep %%build around to document it's intentionally left empty
- Use %%{buildroot} instead of $RPM_BUILD_ROOT

* Fri Oct 27 2006 Luya Tshimbalanga <luya_tfz@thefinalzone.com> - 0.1-5
- Renamed the spec file to respect Packaging Guideline
- Included URL for source
- Cleaned up
- Ajusted permissions
- Removed unneeded build script

* Thu Oct 26 2006 Luya Tshimbalanga <luya_tfz@thefinalzone.com> - 0.1-2
- Minor fixes

* Tue Oct 24 2006 Christopher Aillon <caillon@redhat.com> - 0.1-1
- Initial RPM.

