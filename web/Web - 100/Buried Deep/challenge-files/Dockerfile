FROM python:3.8-slim

RUN useradd -m ctf

WORKDIR /chal

COPY . .

ENV PORT=9998

RUN pip3 install --upgrade --no-cache-dir -r requirements.txt

RUN chown -R ctf:ctf /chal

RUN chmod 750 /chal/server.py && \
    chmod 740 /chal/hidden/flag1.txt && \
    chmod 740 /chal/secret/flag2.txt && \
    chmod 740 /chal/cryptic/flag3.txt && \
    chmod 740 /chal/forbidden/flag4.txt && \
    chmod 740 /chal/buried/flag5.txt && \
    chmod 740 /chal/pvt/flag6.txt && \
    chmod 740 /chal/underground/flag7.txt && \
    chmod 740 /chal/secret_path/flag8.txt && \
    chmod 740 /chal/hidden_flag/flag9.txt && \
    chmod 740 /chal/buried_flag/flag10.txt && \
    chmod 740 /chal/encrypted/flag11.txt

USER ctf

EXPOSE 9998

CMD [ "python3", "/chal/server.py" ]
