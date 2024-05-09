%global octpkg prompt

Summary:	A powerlevel10k-like prompt for octave
Name:		octave-prompt
Version:	0.0.1
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/prompt/
Url:		https://github.com/gnu-octave/prompt
Source0:	https://github.com/gnu-octave/prompt/archive/%{version}/%{octpkg}-%{version}.tar.gz

BuildRequires:  octave-devel

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
A powerlevel10k-like prompt for octave.

%files
%license COPYING
%doc README.md
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

