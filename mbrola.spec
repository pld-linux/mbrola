Summary:	MBROLA is a speech synthesizer based on the concatenation of diphones
Summary(pl):	MBROLA to syntezator mowy bazuj±cy na ³±czeniu dwuzg³osek
Name:		mbrola
Version:	301h?
Release:	1
License:	Non-commercial, non-military purposes, w/ and only w/ the voice and language databases available on http://tcts.fpms.ac.be/synthesis
Group:		Applications/Sound
Source0:	http://tcts.fpms.ac.be/synthesis/mbrola/bin/pclinux/mbr301h.zip
Source1:	http://tcts.fpms.ac.be/synthesis/mbrola/dba/us1/us1-980512.zip
Source2:	http://tcts.fpms.ac.be/synthesis/mbrola/dba/us2/us2-980812.zip
Source3:	http://tcts.fpms.ac.be/synthesis/mbrola/dba/us3/us3-990208.zip
Source4:	http://tcts.fpms.ac.be/synthesis/mbrola/dba/en1/en1-980910.zip
Source5:	http://tcts.fpms.ac.be/synthesis/mbrola/dba/pl1/pl1.zip
URL:		http://tcts.fpms.ac.be/synthesis/mbrola.html

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

%description -l pl
MBROLA jest syntezatorem mowy opartym o po³±czenia dwuzg³osek. Jako
dane wej¶ciowe pobiera listê fonemów, ³±cznie z informacj± prozodyczn±
(d³ugo¶æ fonemów oraz cz±stkowy liniowy opis tonacji), po czym tworzy
16-bitowe (liniowe) próbki mowy o czêstotliwo¶ci próbkowania pobranej
z bazy dwuzg³osek.

NIE jest to syntezator przetwarzaj±cy tekst na mowê (Text-To-Speech,
TTS), gdy¿ nie przyjmuje jako danych wej¶ciowych czystego tekstu. Aby
uzyskaæ pe³ny system TTS trzeba pos³ugiwaæ siê tym syntezatorem
³±cznie z systemem przetwarzania tekstu, który tworzy polecenia
fonetyczno-prozodyczne jako dane wynikowe.

%package voice-us1
Summary:	Files for voice us1 to be used w/ festival
Summary(pl):	Pliki do g³osu us1 przeznaczone dla festival
Group:		Applications/Sound

%description voice-us1

%description voice-us1 -l pl

%prep

%install

rm -rf $RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt

%files voice-us1
%defattr(644,root,root,755)
%{_datadir}/
