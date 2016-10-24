# UVATool
- python3 is required

## install
```bash
 git clone https://github.com/trnila/uvatool.git
 cd uvatool
 virtualenv uva
 source uva/bin/activate
 pip install -r requirements.txt
```

add alias to your shell
`$ alias uva="$(pwd)/uva/bin/python $(pwd)/uva.py" `

## usage
```
 uva init 594
 cd 594
 uva read
 uva test
 echo 12345 > input.in
 uva generate input.in
 uva test
 uva submit
 uva stats
```
