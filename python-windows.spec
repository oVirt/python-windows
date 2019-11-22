Name:		python-windows
Version:	2.7.17
Release:	1%{?dist}
Summary:	RPM wrapper for %{name}
License:	Python
Source:		https://www.python.org/ftp/python/%{version}/python-%{version}.msi
URL:		https://www.python.org/
BuildArch:	noarch

%description
A package wrapping %{name} to provide dependency features.

%prep
install -d %{_builddir}/%{name}
cp -v %{SOURCE0} %{_builddir}/%{name}

%install
DST=%{buildroot}%{_datadir}/%{name}/
mkdir -p $DST
cp -v %{_builddir}/%{name}/* $DST

%files
%{_datadir}/%{name}

%changelog
* Fri Nov 22 2019 Sandro Bonazzola <sbonazzo@redhat.com> - 2.7.17-1
- Rebased on Python 2.7.17

* Tue Oct 10 2017 Sandro Bonazzola <sbonazzo@redhat.com> - 2.7.14-1
- Rebased on Python 2.7.14

* Fri Sep  2 2016 Sandro Bonazzola <sbonazzo@redhat.com> - 2.7.12-1
- Rebased on Python 2.7.12

* Tue Oct 20 2015 Yedidyah Bar David <didi@redhat.com> 2.7.8-2
- dropped "artifacts" from all paths

* Wed Oct 08 2014 Lev Veyde <lveyde@redhat.com> 2.7.8-1
- Initial version
