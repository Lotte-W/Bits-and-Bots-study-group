@echo off
for %%f in (H:\Demo_cmd\literature\*) do (
    certutil -hashfile "%%f" SHA256
)


