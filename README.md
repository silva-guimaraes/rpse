um quebra galhos pra quando alguma série ou filme vem com as legendas separadas e eu preciso que o tocador de video automaticamente selecione as legendas corretas.

```sh
# pasta de séries:
01_primeiro_episódio.mkv 
02_segundo_episódio.mkv 
03_terceiro_episódio.mkv 
04_quarto_episódio.mkv 
05_quinto_episódio.mkv 
01_first_subtitle_file.srt
02_second_subtitle_file.srt
03_third_subtitle_file.srt
04_forth_subtitle_file.srt
05_fifth_subtitle_file.srt
```
```sh
rpse '01_primeiro_episódio.mkv' '01_first_subtitle_file.srt'
```
``` 
01_primeiro_episódio.mkv 
01_primeiro_episódio.srt 
02_segundo_episódio.mkv 
02_segundo_episódio.srt 
03_terceiro_episódio.mkv 
03_terceiro_episódio.srt 
04_quarto_episódio.mkv 
04_quarto_episódio.srt 
05_quinto_episódio.mkv 
05_quinto_episódio.srt
```
a funcionalidade padrão serve apenas quando os arquivos podem ser ordenados em ordem alfabética. se isso não for possivel eu tambem inclui uma opção que aceita uma ordem customizada usando arquivos de texto
``` sh
# eps.txt
primeiro_episódio.mkv 
segundo_episódio.mkv 
terceiro_episódio.mkv 
quarto_episódio.mkv 
quinto_episódio.mkv 
``` 
```sh
# subs.txt
first_subtitle_file.srt
second_subtitle_file.srt
third_subtitle_file.srt
forth_subtitle_file.srt
fifth_subtitle_file.srt
# legendas ficariam desse modo em ordem alfabética
# fifth_subtitle_file.srt
# first_subtitle_file.srt
# forth_subtitle_file.srt
# second_subtitle_file.srt
# third_subtitle_file.srt
```
```sh
rpse 'eps.txt' 'subs.txt' -txt
```

