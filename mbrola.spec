# NOTE:
# - x86_64 version is actually 3.01d & 32bit @ http://tcts.fpms.ac.be/synthesis/mbrola/bin/amd64linux/mbrola.zip
# - real amd64 version says archidecture panic:
#   http://tcts.fpms.ac.be/synthesis/mbrola/bin/amd64linux/mbrola_AMD_Linux.zip
Summary:	MBROLA - a speech synthesizer based on the concatenation of diphones
Summary(pl.UTF-8):	MBROLA - syntezator mowy bazujący na łączeniu dwuzgłosek
Name:		mbrola
Version:	301h
Release:	8
License:	Non-commercial, non-military purposes, w/ and only w/ the voice and language databases available on http://tcts.fpms.ac.be/synthesis/
Group:		Applications/Sound
Source0:	http://tcts.fpms.ac.be/synthesis/mbrola/bin/pclinux/mbr%{version}.zip
# Source0-md5:	95314c9a545918729a5965f86859a28e
URL:		http://tcts.fpms.ac.be/synthesis/mbrola.html
BuildRequires:	unzip
ExclusiveArch:	%{ix86} ppc alpha sparc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# binaries are without debuginfo
%define		_enable_debug_packages	0

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
%setup -q -c -T -a 0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%ifarch %{ix86}
install -p mbrola-linux-i386 $RPM_BUILD_ROOT%{_bindir}/mbrola
%endif
%ifarch ppc
install -p mbrola302b-linux-ppc $RPM_BUILD_ROOT%{_bindir}/mbrola
%endif
%ifarch alpha
install -p mbrola-linux-alpha $RPM_BUILD_ROOT%{_bindir}/mbrola
%endif
%ifarch sparc
install -p mbrola-SuSElinux-ultra1.dat $RPM_BUILD_ROOT%{_bindir}/mbrola
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/mbrola
