%define name referencer
%define version 1.0.3
%define release %mkrel 1

Summary: Bibliography reference management tool for GNOME
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
# 48x48 PNG from referencer.svg in package, generated with GIMP
Source1: referencer.png
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
BuildRequires: ImageMagick

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
# the MIME database from being generated, but it's broken in 1.0.3. So using
# this dirty workaround. If updating this package, please check whether
# --disable-update-mime-database option is working, and use that instead of
# this hack if it is.
rm -rf $RPM_BUILD_ROOT/%_datadir/mime

# fd.o icons
mkdir -p %buildroot%{_iconsdir}/hicolor/{48x48,32x32,16x16}/apps
cp %buildroot%_datadir/pixmaps/%name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
cp %SOURCE1 %buildroot%_iconsdir/hicolor/48x48/apps/%name.png
convert -scale 32 %SOURCE1 %buildroot%_iconsdir/hicolor/32x32/apps/%name.png
convert -scale 16 %SOURCE1 %buildroot%_iconsdir/hicolor/16x16/apps/%name.png
# MDV icons
mkdir -p %buildroot{%_liconsdir,%_miconsdir}
cp %SOURCE1 %buildroot%_liconsdir/%name.png
convert -scale 32 %SOURCE1 %buildroot%_iconsdir/%name.png
convert -scale 16 %SOURCE1 %buildroot%_miconsdir/%name.png

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Office-Accesories" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

sed -e 's/%{name}.svg/%{name}/' %buildroot%{_datadir}/applications/%{name}.desktop > %buildroot%{_datadir}/applications/%{name}.new && \
mv -f %buildroot%{_datadir}/applications/%{name}.new %buildroot%{_datadir}/applications/%{name}.desktop

%find_lang %name

%post
%update_icon_cache hicolor
%update_menus
%update_mime_database
%postun
%clean_icon_cache hicolor
%clean_menus
%clean_desktop_database

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog TODO
%_bindir/%{name}
%_datadir/applications/%{name}.desktop
%_datadir/%{name}/*
%_iconsdir/*
%_liconsdir/*
%_miconsdir/*
%_datadir/pixmaps/referencer.svg
