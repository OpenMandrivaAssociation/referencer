%define name	referencer
%define version	1.0.4
%define release	%mkrel 2

Summary:	Bibliography reference management tool for GNOME
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
# 48x48 PNG from referencer.svg in package, generated with GIMP
Source1:	referencer.png
# French translation from Launchpad: 
# https://translations.launchpad.net/referencer/trunk/+pots/referencer/fr/
Source2:	fr.po
# From upstream SVN: adapts to poppler 0.6
Patch0:		referencer-1.0.4-poppler.patch
License:	GPLv2
Group:		Graphical desktop/GNOME
URL:		http://icculus.org/referencer/index.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libpopplerglib-devel
BuildRequires:	gtkmm2.4-devel
BuildRequires:	libgnomeuimm2.6-devel
BuildRequires:	gnome-vfsmm2.6-devel
BuildRequires:	libglademm2.4-devel
BuildRequires:	gconfmm2.6-devel
BuildRequires:	libboost-devel
BuildRequires:	desktop-file-utils
BuildRequires:	ImageMagick

%description
Referencer is a GNOME application to organise documents or references, and 
ultimately generate a BibTeX bibliography file.

%prep
%setup -q
%patch0 -p1 -b .poppler
install -m 644 %{SOURCE2} po/fr.po
echo fr >> po/LINGUAS

%build
%configure --disable-update-mime-database
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# fd.o icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{scalable,48x48,32x32,16x16}/apps
install -m 644 %{buildroot}%{_datadir}/pixmaps/%{name}.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
install -m 644 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert -scale 32 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
# MDV icons
mkdir -p %{buildroot}{%{_liconsdir},%{_miconsdir}}
install -m 644 %{SOURCE1} %{buildroot}%{_liconsdir}/%{name}.png
convert -scale 32 %{SOURCE1} %{buildroot}%{_iconsdir}/%{name}.png
convert -scale 16 %{SOURCE1} %{buildroot}%{_miconsdir}/%{name}.png

# menu
perl -pi -e 's,%{name}.svg,%{name},g' %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %{name}

%post
%{update_icon_cache hicolor}
%{update_menus}
%{update_mime_database}
%postun
%{clean_icon_cache hicolor}
%{clean_menus}
%{clean_desktop_database}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_iconsdir}/hicolor/48x48/mimetypes/gnome-mime-application-x-%{name}.png
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/mime/packages/%{name}.xml
