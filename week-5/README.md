## 要求三：SQL CRUD
● 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。

● 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
![image](https://user-images.githubusercontent.com/95182061/151557950-a1fe5201-3d90-441b-9c13-77b0791e04a5.png)
● 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
![image](https://user-images.githubusercontent.com/95182061/151558768-f708e11b-03ca-4d84-bc69-eac7dac3cb53.png)
● 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。
![image](https://user-images.githubusercontent.com/95182061/151562317-59c0ab72-d071-49ff-8b41-8f721f5bfd8e.png)
● 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
![image](https://user-images.githubusercontent.com/95182061/151562858-01bb8450-7a9f-41b1-b4aa-4c32820207df.png)
● 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
![image](https://user-images.githubusercontent.com/95182061/151563121-8573b825-d659-4e5f-8a47-750c42ab1ad0.png)
●使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
![image](https://user-images.githubusercontent.com/95182061/151563547-8a215ca8-d1ae-40c0-9e30-e9009d9e1224.png)
## 要求四：SQL Aggregate Functions
● 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
![image](https://user-images.githubusercontent.com/95182061/151564683-80742175-0019-430f-9714-ad5b354bfecf.png)
● 取得 member 資料表中，所有會員 follower_count 欄位的總和。
![image](https://user-images.githubusercontent.com/95182061/151565083-fe8d11cd-1857-4bcb-a743-7ee667ec8df7.png)
● 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
![image](https://user-images.githubusercontent.com/95182061/151565418-62b5b235-3a15-4286-a246-b88619b14d89.png)
## 要求五：SQL JOIN (Optional)
● 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
![image](https://user-images.githubusercontent.com/95182061/151599798-d4845ea2-6e81-425b-bdbe-8f331455b5fa.png)
● 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。
![image](https://user-images.githubusercontent.com/95182061/151600511-0865fe82-2815-4a48-983c-1d4400238a4b.png)

