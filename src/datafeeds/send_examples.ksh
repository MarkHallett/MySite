# send_examples.ksh

export CCY_PAIR_NAME=GBP/USD
export CCY_PAIR_VALUE=1.23
#python send_example_data.py



run_container(){
  name=$1
  value=$2

  #echo $name, $value

  docker run -i -t \
     -e CCY_PAIR_NAME=$name \
     -e CCY_PAIR_VALUE=$value \
     -e MR_RABITMQ=${MR_RABITMQ} \
     markhallett/send_example_data
}

run_container "GBP/USD" 1.0
read
run_container "GBP/USD" 1.1
read
run_container "GBP/USD" 1.2
read
run_container "USD/EUR" 1.33
read
run_container "USD/EUR" 1.23
read
run_container "EUR/GBP" 0.33
read
run_container "EUR/GBP" 0.39
read
run_container "GBP/USD" 0.8
read
run_container "USD/EUR" 0.9
read
run_container "EUR/GBP" 0.5
read
run_container "EUR/GBP" 0.0
read
run_container "EUR/GBP" 0.33
read
run_container "EUR/GBP" 5.55
read
run_container "EUR/GBP" 0.88
