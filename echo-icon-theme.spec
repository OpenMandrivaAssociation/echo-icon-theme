%define git_head_full 51c5760509be39d0c1e11d904cf44eef79a80b2e
%define git_head 51c57605

Name:           echo-icon-theme
Version:        0.3.89.0
Release:        %mkrel 0.git%{git_head}.1
Summary:        Echo icon theme

Group:          Graphical desktop/Other
License:        Creative Commons Attribution-ShareAlike 3.0
URL:            http://fedoraproject.org/wiki/Artwork/EchoDevelopment
Source0:        %{name}-%{git_head_full}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
Requires(post): gtk2 >= 2.6.0
Requires(postun): gtk2 >= 2.6.0
BuildRequires: icon-naming-utils >= 0.8.1
Requires:       gnome-icon-theme

#for Clearlooks icon theme dependency
Requires:       gnome-themes

%description
This package contains the Echo icon theme from Fedora.


%prep
%setup -q -n %{name}
%{_bindir}/autoreconf --install

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
touch %{buildroot}%{_datadir}/icons/Echo/icon-theme.cache

%post
%update_icon_cache Echo

%postun
%clean_icon_cache Echo

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING
%dir %{_datadir}/icons/Echo
%{_datadir}/icons/Echo/index.theme
%_datadir/icons/Echo/??x??/
%_datadir/icons/Echo/scalable
%ghost %_datadir/icons/Echo/icon-theme.cache


