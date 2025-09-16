#
# TODO: Fix custom CFLAGS
#
Summary:	MBROLA - a speech synthesizer based on the concatenation of diphones
Summary(pl.UTF-8):	MBROLA - syntezator mowy bazujący na łączeniu dwuzgłosek
Name:		mbrola
Version:	3.3
Epoch:		1
Release:	1
License:	AGPL v3+
Group:		Applications/Sound
Source0:	https://github.com/numediart/MBROLA/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	06993903c7b8d3a8d21cc66cd5a28219
URL:		https://github.com/numediart/MBROLA
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MBROLA is a speech synthesizer based on the concatenation of diphones.
It takes a list of phonemes as input, together with prosodic
information (duration of phonemes and a piecewise linear description
of pitch), and produces speech samples on 16 bits (linear), at the
sampling frequency of the diphone database.

It is therefore NOT a Text-To-Speech (TTS) synthesizer, since it does
not accept raw text as input. In order to obtain a full TTS system,
you need to use this synthesizer in combination with a text processing
system that produces phonetic and prosodic commands.

%description -l pl.UTF-8
MBROLA jest syntezatorem mowy opartym o połączenia dwuzgłosek. Jako
dane wejściowe pobiera listę fonemów, łącznie z informacją prozodyczną
(długość fonemów oraz cząstkowy liniowy opis tonacji), po czym tworzy
16-bitowe (liniowe) próbki mowy o częstotliwości próbkowania pobranej
z bazy dwuzgłosek.

NIE jest to syntezator przetwarzający tekst na mowę (Text-To-Speech,
TTS), gdyż nie przyjmuje jako danych wejściowych czystego tekstu. Aby
uzyskać pełny system TTS trzeba posługiwać się tym syntezatorem
łącznie z systemem przetwarzania tekstu, który tworzy polecenia
fonetyczno-prozodyczne jako dane wynikowe.

%prep
%setup -q -n MBROLA-%{version}

export CC=%{__cc}
export CFLAGS"=%{rpmcflags}"
%{__make} version
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp -p Bin/mbrola $RPM_BUILD_ROOT%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/mbrola
