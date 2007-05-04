%define alphatag 20070419wiki

Name:           echo-icon-theme
Version:        0.2
Release:        %mkrel 0.%{alphatag}.1
Summary:        Echo icon theme

Group:          Graphical desktop/Other
License:        Creative Commons Attribution-ShareAlike 2.5
URL:            http://fedoraproject.org/wiki/Artwork/EchoDevelopment
Source0:        %{name}-%{version}-%{alphatag}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
Requires(post): gtk2 >= 2.6.0
Requires(postun): gtk2 >= 2.6.0

%description
This package contains the Echo icon theme from Fedora 7.


%prep
%setup -q -n %{name}-%{version}-%{alphatag}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/icons
cp -r --preserve=timestamps Echo %{buildroot}%{_datadir}/icons

touch %buildroot%_datadir/icons/Echo/icon-theme.cache

%post
%update_icon_cache Echo

%postun
%clean_icon_cache Echo

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc LICENSE
%dir %{_datadir}/icons/Echo
%{_datadir}/icons/Echo/index.theme
%_datadir/icons/Echo/??x??/
%ghost %_datadir/icons/Echo/icon-theme.cache


