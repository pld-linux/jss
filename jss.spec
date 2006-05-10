# TODO: fix JNI build
Summary:	JSS - Network Security Services for Java
Summary(pl):	JSS - Network Security Services for Java - usługi bezpieczeństwa sieciowego dla Javy
Name:		jss
Version:	3.4.1
Release:	1
License:	NPL 1.1
Group:		Development/Languages/Java
Source0:	ftp://ftp.mozilla.org/pub/mozilla.org/security/jss/releases/JSS_3_4_1_RTM/src/%{name}-%{version}-src.tar.gz
# Source0-md5:	29689ea36b27584feb22d291404506ea
URL:		http://www.mozilla.org/projects/security/pki/jss/
BuildRequires:	jdk
BuildRequires:	nspr-devel >= 2.0
BuildRequires:	nss-devel
BuildRequires:	perl-base
BuildRequires:	sed >= 4.0
Requires:	jre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
A Java interface to NSS that supports most of the security standards
and encryption technologies supported by NSS. JSS also provides a pure
Java interface for ASN.1 types and BER/DER encoding.

%description -l pl
Interfejs Javy do biblioteki NSS obsługujący większość standardów
bezpieczeństwa i technologii szyfrowania obsługiwanych przez NSS. JSS
udostępnia także czysto javowy interfejs do typów ASN.1 i kodowania
BER/DER.

%prep
%setup -q -n %{name}-%{version}-src

sed -i -e 's/-O/-O -source 1.4/' mozilla/security/jss/build_java.pl

%build
%{__make} -C mozilla/security/coreconf \
	BUILD_OPT=1 \
	CC="%{__cc}" \
	OPTIMIZER="%{rpmcflags}"
%{__make} -C mozilla/security/jss \
	BUILD_OPT=1 \
	CC="%{__cc}" \
	JAVA_HOME=%{_libdir}/java \
	OPTIMIZER="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}

install mozilla/dist/xpclass.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf xpclass.jar $RPM_BUILD_ROOT%{_javalibdir}/jss.jar

# TODO: JNI library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc mozilla/security/jss/jss.html
%{_javalibdir}/*.jar
