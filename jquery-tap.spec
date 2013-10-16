%define		plugin	tap
Summary:	jQuery plugin that creates a click alternative for touch enabled browsers
Name:		jquery-%{plugin}
Version:	1.0.2
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	http://github.com/aarongloege/jquery.tap/archive/%{version}/%{plugin}-%{version}.tar.gz
# Source0-md5:	0414e5d1287e8ac9a96a8f495432a086
URL:		http://plugins.jquery.com/tap/
Requires:	jquery >= 1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
A jQuery plugin that creates a click alternative for touch enabled
browsers. Click events on touch devices do not work the best. There is
a 300ms delay from when you release your finger to the time the click
event is triggered. This behavior is not desired. What is nice about
this plugin, and what makes it different from other plugins, is that
it takes advantage of jQuery's special event API, so you can use
jQuery.on to bind events. And, because the event is bound through
jQuery's on API, you can take advantage of namespaces and delegate
events.

%package demo
Summary:	Demo for jQuery.%{plugin}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.%{plugin}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery.%{plugin}.

%prep
%setup -q -n jquery.%{plugin}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}

cp -p jquery.%{plugin}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
cp -p jquery.%{plugin}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
ln -s %{plugin}-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.min.js

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENCE
%{_appdir}

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
