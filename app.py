import os
import subprocess

def create_symlink(source, target_directory):
    try:
        if not os.path.exists(source):
            print(f"源路径不存在: {source}")
            return
        source_name = os.path.basename(source)

        target = os.path.join(target_directory, source_name)

        if os.path.exists(target):
            print(f"目标路径已存在: {target}")
            overwrite = input("是否覆盖目标路径？(y/n): ").strip().lower()
            if overwrite != "y":
                print("操作取消")
                return
            os.remove(target)

        subprocess.run(["ln", "-s", source, target], check=True)
        print(f"符号链接已创建: {source} -> {target}")
    except subprocess.CalledProcessError as e:
        print(f"创建符号链接失败: {e}")
    except Exception as e:
        print(f"发生错误: {e}")

def main():
    print("创建符号链接 (ln -s)")
    source = input("请输入源路径: ").strip().replace("'", "")
    target_directory = input("请输入目标目录: ").strip().replace("'", "")
    create_symlink(source, target_directory)

if __name__ == "__main__":
    main()
