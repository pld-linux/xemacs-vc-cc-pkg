Summary:	Version Control for ClearCase (UnFree) systems
Summary(pl):	Kontrola wersji dla systemów ClearCase (nie-wolnych)
Name:		xemacs-vc-cc-pkg
%define 	srcname	vc-cc
Version:	1.16
Release:	2
License:	GPL
Group:		Applications/Editors/Emacs
Group(de):	Applikationen/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-dired-pkg
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Version Control for ClearCase (UnFree) systems.

%description -l pl 
Kontrola wersji dla systemów ClearCase (nie-wolnych).

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

gzip -9nf lisp/vc-cc/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/vc-cc/ChangeLog.gz 
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
