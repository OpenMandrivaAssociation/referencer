Summary:	Bibliography reference management tool for GNOME
Name:		referencer
Version:	1.1.5
Release:	%mkrel 4
Source0:	http://icculus.org/referencer/downloads/%{name}-%{version}.tar.gz
# 48x48 PNG from referencer.svg in package, generated with GIMP
Source1:	referencer.png
License:	GPLv2
Group:		Graphical desktop/GNOME
URL:		http://icculus.org/referencer/index.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libpoppler-glib-devel
BuildRequires:	gtkmm2.4-devel
BuildRequires:	libgnomeuimm2.6-devel
BuildRequires:	gnome-vfsmm2.6-devel
BuildRequires:	libglademm2.4-devel
BuildRequires:	gconfmm2.6-devel
BuildRequires:	libboost-devel
BuildRequires:	desktop-file-utils
BuildRequires:	python-devel
BuildRequires:	imagemagick
BuildRequires:	intltool

%description
Referencer is a GNOME application to organise documents or references, and 
ultimately generate a BibTeX bibliography file.

%prep
%setup -q

%build
%configure2_5x --disable-update-mime-database
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

# menu
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_icon_cache hicolor}
%{update_menus}
%{update_mime_database}
%endif
%if %mdkversion < 200900
%postun
%{clean_icon_cache hicolor}
%{clean_menus}
%{clean_mime_database}
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README AUTHORS ChangeLog TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_iconsdir}/hicolor/48x48/mimetypes/gnome-mime-application-x-%{name}.png
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/mime/packages/%{name}.xml
