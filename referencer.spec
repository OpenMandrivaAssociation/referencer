%define name referencer
%define version 1.0.2
%define release %mkrel 2

Summary: Bibliography reference management tool for GNOME
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Graphical desktop/GNOME
Url: http://icculus.org/referencer/index.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libpoppler-devel
BuildRequires: gtkmm2.4-devel
BuildRequires: libgnomeuimm2.6-devel
BuildRequires: gnome-vfsmm2.6-devel
BuildRequires: libglademm2.4-devel
BuildRequires: gconfmm2.6-devel
BuildRequires: libboost-devel
BuildRequires: desktop-file-utils

%description
Referencer is a Gnome application to organise documents or references, and 
ultimately generate a BibTeX bibliography file.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
# There's a --disable-update-mime-database option to configure which stops
# the MIME database from being generated, but it's broken in 1.0.2. So using
# this dirty workaround. If updating this package, please check whether
# --disable-update-mime-database option is working, and use that instead of
# this hack if it is.
rm -rf $RPM_BUILD_ROOT/%_datadir/mime
%find_lang %name
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Office-Accesories" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*
%post
%update_icon_cache hicolor
%update_menus
%postun
%clean_icon_cache hicolor
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog TODO
%_bindir/%{name}
%_datadir/applications/%{name}.desktop
%_datadir/%{name}/*
%_datadir/icons/hicolor/48x48/mimetypes/gnome-mime-application-x-referencer.png
%_datadir/pixmaps/referencer.svg


