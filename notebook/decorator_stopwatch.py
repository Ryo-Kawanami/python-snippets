# デコレータを用いて関数処理時間を計測する
import time

def stopwatch(func):
  # 実行したい処理を記述
  def wrapper(*args, **kwargs):
    start = time.time()  # 現在時刻（処理開始前）を取得
    result = func(*args, **kwargs)
    end = time.time()  # 現在時刻（処理完了後）を取得
    time_diff = end - start  # 処理完了後の時刻から処理開始前の時刻を減算する
    print(f'処理時間 = {time_diff : .10f} sec')
    return result  # 処理にかかった時間データを使用
  return wrapper

@stopwatch
def add_num(a, b):
  sum = a + b
  return sum

print(add_num(1, 2))

# 実行コマンド： python3 decorator_stopwatch.py
# 結果： 
# 処理時間 =  0.0000011921 sec
# 3
