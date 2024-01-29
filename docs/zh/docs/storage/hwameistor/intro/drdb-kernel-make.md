---
hide:
  - toc
---

# DRBD 自助编译操作

当 DRBD 默认适配的内核版本不支持时，建议参考该文档的步骤，来编译对应的离线包并安装到对应环境中来使用 DRBD 的功能。

## 操作步骤

本文以内核为 `4.9.212-36.el7.x86_64` 为例进行演示。

### 编译内核

1. 确认内核版本

    ```bash
      uname -r
    ```

    输出结果为 `Linux localhost.localdomain 4.9.212-36.el7.x86_64 #1 SMP Thu Feb 6 17:55:02 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux`

1. 下载源码

    ```bash
    wget https://pkg.linbit.com//downloads/drbd/9.0/drbd-9.0.32-1.tar.gz

    tar -xvf drbd-9.0.32-1.tar.gz
    ```

1. 下载安装内核编译模块

    ```bash
    # 下载 rpm 包，其他内核的可前往 https://linux.cc.iitk.ac.in/mirror/centos/elrepo/kernel/el7/x86_64/RPMS/ 查看
    wget https://linux.cc.iitk.ac.in/mirror/centos/7/virt/x86_64/xen-common/Packages/k/kernel-4.9.212-36.el7.x86_64.rpm
    # 安装
    rpm -ivh kernel-devel-4.9.212-36.el7.x86_64.rpm
    ```

    安装完执行检查

    ```bash
    $ ls -lF /lib/modules/`uname -r`/build
    lrwxrwxrwx. 1 root root 38 Dec  5 13:47 /lib/modules/4.9.212-36.el7.x86_64/build -> /usr/src/kernels/4.9.212-36.el7.x86_64/
    $ ls -lF /lib/modules/`uname -r`/source
    lrwxrwxrwx. 1 root root 5 Dec  5 13:14 /lib/modules/4.9.212-36.el7.x86_64/source -> build/
    ```

1. 下载安装编译所需依赖

    安装 gcc、make、patch、kmod、cpio、python3以及python3-pip 软件包

    ```bash
    yum install -y gcc make patch kmod cpio python3 python3-pip
    ```

    安装 coccinelle

    ```bash
    git clone https://github.com/coccinelle/coccinelle.git
    yum install -y ocaml ocaml-native-compilers ocaml-findlib menhir automake
    ./autogen
    ./configure
    sudo make install
    ```

1. 开始编译

    a. 进入到 `drbd-9.0.32-1` 目录下执行 `make` 命令，输出结果如下：

        ```bash
        Calling toplevel makefile of kernel source tree, which I believe is in
        KDIR=/lib/modules/4.9.212-36.el7.x86_64/source
    
        make -C /lib/modules/4.9.212-36.el7.x86_64/source  O=/lib/modules/4.9.212-36.el7.x86_64/build M=/home/drbd-9.0.32-1/drbd  modules
        COMPAT  __vmalloc_has_2_params
        COMPAT  alloc_workqueue_takes_fmt
        COMPAT  before_4_13_kernel_read
        COMPAT  blkdev_issue_zeroout_discard
        COMPAT  can_include_vermagic_h
        COMPAT  drbd_release_returns_void
        COMPAT  genl_policy_in_ops
        COMPAT  have_BIO_MAX_VECS
        COMPAT  have_CRYPTO_TFM_NEED_KEY
        COMPAT  have_SHASH_DESC_ON_STACK
        COMPAT  have_WB_congested_enum
        COMPAT  have_allow_kernel_signal
        COMPAT  have_atomic_dec_if_positive_linux
        COMPAT  have_atomic_in_flight
        COMPAT  have_bd_claim_by_disk
        COMPAT  have_bd_unlink_disk_holder
        COMPAT  have_bdi_cap_stable_writes
        COMPAT  have_bdi_congested_fn
        COMPAT  have_bio_bi_bdev
        COMPAT  have_bio_bi_error
        COMPAT  have_bio_bi_opf
        COMPAT  have_bio_bi_status
        COMPAT  have_bio_clone_fast
        COMPAT  have_bio_flush
        COMPAT  have_bio_free
        COMPAT  have_bio_op_shift
        COMPAT  have_bio_rw
        COMPAT  have_bio_set_dev
        COMPAT  have_bio_set_op_attrs
        COMPAT  have_bio_start_io_acct
        COMPAT  have_bioset_create_front_pad
        COMPAT  have_bioset_init
        COMPAT  have_bioset_need_bvecs
        COMPAT  have_blk_alloc_disk
        COMPAT  have_blk_alloc_queue_rh
        COMPAT  have_blk_check_plugged
        COMPAT  have_blk_qc_t_make_request
        COMPAT  have_blk_queue_flag_set
        COMPAT  have_blk_queue_make_request
        COMPAT  have_blk_queue_merge_bvec
        COMPAT  have_blk_queue_plugged
        COMPAT  have_blk_queue_split_bio
        COMPAT  have_blk_queue_split_q_bio
        COMPAT  have_blk_queue_split_q_bio_bioset
        COMPAT  have_blk_queue_update_readahead
        COMPAT  have_blk_queue_write_cache
        COMPAT  have_blkdev_get_by_path
        COMPAT  have_d_inode
        COMPAT  have_fallthrough
        COMPAT  have_file_inode
        COMPAT  have_generic_start_io_acct_q_rw_sect_part
        COMPAT  have_generic_start_io_acct_rw_sect_part
        COMPAT  have_genl_family_parallel_ops
        COMPAT  have_hd_struct
        COMPAT  have_ib_cq_init_attr
        COMPAT  have_ib_get_dma_mr
        COMPAT  have_idr_alloc
        COMPAT  have_idr_is_empty
        COMPAT  have_inode_lock
        COMPAT  have_ktime_to_timespec64
        COMPAT  have_kvfree
        COMPAT  have_max_send_recv_sge
        COMPAT  have_netlink_cb_portid
        COMPAT  have_nla_nest_start_noflag
        COMPAT  have_nla_parse_deprecated
        COMPAT  have_nla_put_64bit
        COMPAT  have_nla_strscpy
        COMPAT  have_part_stat_h
        COMPAT  have_part_stat_read_accum
        COMPAT  have_pointer_backing_dev_info
        COMPAT  have_prandom_u32
        COMPAT  have_proc_create_single
        COMPAT  have_queue_flag_stable_writes
        COMPAT  have_ratelimit_state_init
        COMPAT  have_rb_augment_functions
        COMPAT  have_refcount_inc
        COMPAT  have_req_flush
        COMPAT  have_req_hardbarrier
        COMPAT  have_req_noidle
        COMPAT  have_req_nounmap
        COMPAT  have_req_op_write
        COMPAT  have_req_op_write_same
        COMPAT  have_req_op_write_zeroes
        COMPAT  have_req_prio
        COMPAT  have_req_write
        COMPAT  have_req_write_same
        COMPAT  have_revalidate_disk_size
        COMPAT  have_sched_set_fifo
        COMPAT  have_security_netlink_recv
        COMPAT  have_sendpage_ok
        COMPAT  have_set_capacity_and_notify
        COMPAT  have_shash_desc_zero
        COMPAT  have_signed_nla_put
        COMPAT  have_simple_positive
        COMPAT  have_sock_set_keepalive
        COMPAT  have_struct_bvec_iter
        COMPAT  have_struct_kernel_param_ops
        COMPAT  have_struct_size
        COMPAT  have_submit_bio
        COMPAT  have_submit_bio_noacct
        COMPAT  have_tcp_sock_set_cork
        COMPAT  have_tcp_sock_set_nodelay
        COMPAT  have_tcp_sock_set_quickack
        COMPAT  have_time64_to_tm
        COMPAT  have_timer_setup
        COMPAT  have_void_make_request
        COMPAT  hlist_for_each_entry_has_three_parameters
        COMPAT  ib_alloc_pd_has_2_params
        COMPAT  ib_device_has_ops
        COMPAT  ib_post_send_const_params
        COMPAT  ib_query_device_has_3_params
        COMPAT  kmap_atomic_page_only
        COMPAT  need_make_request_recursion
        COMPAT  part_stat_read_takes_block_device
        COMPAT  queue_limits_has_discard_zeroes_data
        COMPAT  rdma_create_id_has_net_ns
        COMPAT  sock_create_kern_has_five_parameters
        COMPAT  sock_ops_returns_addr_len
        CHK     /home/drbd-9.0.32-1/drbd/compat.4.9.212-36.el7.x86_64.h
        UPD     /home/drbd-9.0.32-1/drbd/compat.4.9.212-36.el7.x86_64.h
        CHK     /home/drbd-9.0.32-1/drbd/compat.h
        UPD     /home/drbd-9.0.32-1/drbd/compat.h
        make[4]: `drbd-kernel-compat/cocci_cache/a707960de8e44ee768894d4f66792d36/compat.patch' is up to date.
          PATCH
        patching file ./drbd_int.h
        patching file ./drbd_req.h
        patching file drbd-headers/linux/genl_magic_struct.h
        patching file drbd_state.c
        patching file drbd_receiver.c
        patching file drbd_main.c
        patching file drbd_nla.c
        patching file drbd_nl.c
        patching file drbd_bitmap.c
        patching file drbd_sender.c
        patching file drbd_transport_tcp.c
        patching file drbd_actlog.c
        patching file kref_debug.c
        patching file drbd_req.c
        patching file drbd_debugfs.c
        patching file drbd-headers/linux/genl_magic_func.h
        Hunk #2 succeeded at 312 (offset -20 lines).
          CC [M]  /home/drbd-9.0.32-1/drbd/drbd_debugfs.o
          CC [M]  /home/drbd-9.0.32-1/drbd/drbd_bitmap.o
          CC [M]  /home/drbd-9.0.32-1/drbd/drbd_proc.o
          CC [M]  /home/drbd-9.0.32-1/drbd/drbd_sender.o
          CC [M]  /home/drbd-9.0.32-1/drbd/drbd_receiver.o
          CC [M]  /home/drbd-9.0.32-1/drbd/drbd_req.o
          CC [M]  /home/drbd-9.0.32-1/drbd/drbd_actlog.o
          CC [M]  /home/drbd-9.0.32-1/drbd/lru_cache.o
          CC [M]  /home/drbd-9.0.32-1/drbd/drbd_main.o
          CC [M]  /home/drbd-9.0.32-1/drbd/drbd_strings.o
          CC [M]  /home/drbd-9.0.32-1/drbd/drbd_nl.o
          CC [M]  /home/drbd-9.0.32-1/drbd/drbd_interval.o
          CC [M]  /home/drbd-9.0.32-1/drbd/drbd_state.o
          CC [M]  /home/drbd-9.0.32-1/drbd/drbd-kernel-compat/drbd_wrappers.o
          CC [M]  /home/drbd-9.0.32-1/drbd/drbd_nla.o
          CC [M]  /home/drbd-9.0.32-1/drbd/drbd_transport.o
          GEN     /home/drbd-9.0.32-1/drbd/drbd_buildtag.c
          CC [M]  /home/drbd-9.0.32-1/drbd/drbd_buildtag.o
          LD [M]  /home/drbd-9.0.32-1/drbd/drbd.o
          CC [M]  /home/drbd-9.0.32-1/drbd/drbd_transport_tcp.o
          Building modules, stage 2.
          MODPOST 2 modules
          CC      /home/drbd-9.0.32-1/drbd/drbd.mod.o
          LD [M]  /home/drbd-9.0.32-1/drbd/drbd.ko
          CC      /home/drbd-9.0.32-1/drbd/drbd_transport_tcp.mod.o
          LD [M]  /home/drbd-9.0.32-1/drbd/drbd_transport_tcp.ko
          mv .drbd_kernelrelease.new .drbd_kernelrelease
          Memorizing module configuration ... done.
         ```

  b. 创建目录 `/lib/modules/<内核版本>/kernel/drivers/block/drbd/`，内核版本根据实际情况替换

  c. 把上一步编译后生成的 `/home/drbd-9.0.32-1/drbd/drbd.ko`、`/home/drbd-9.0.32-1/drbd/drbd_transport_tcp.ko` 传至  `/lib/modules/<内核版本>/kernel/drivers/block/drbd/`

  d. 配置conf，创建目录把 `global_common.conf` 放在 `/etc/drbd.d/` 目录下，`drbd.conf` 放在 `/etc` 目录下：

       global_common.conf 文件

       ```bash
        # DRBD is the result of over a decade of development by LINBIT.
        # In case you need professional services for DRBD or have
        # feature requests visit http://www.linbit.com
        
        global {
                usage-count yes;
        
                # Decide what kind of udev symlinks you want for "implicit" volumes
                # (those without explicit volume <vnr> {} block, implied vnr=0):
                # /dev/drbd/by-resource/<resource>/<vnr>   (explicit volumes)
                # /dev/drbd/by-resource/<resource>         (default for implict)
                udev-always-use-vnr; # treat implicit the same as explicit volumes
        
                # minor-count dialog-refresh disable-ip-verification
                # cmd-timeout-short 5; cmd-timeout-medium 121; cmd-timeout-long 600;
        }
        
        common {
                handlers {
                        # These are EXAMPLE handlers only.
                        # They may have severe implications,
                        # like hard resetting the node under certain circumstances.
                        # Be careful when choosing your poison.
        
                        # pri-on-incon-degr "/usr/lib/drbd/notify-pri-on-incon-degr.sh; /usr/lib/drbd/notify-emergency-reboot.sh; echo b > /proc/sysrq-trigger ; reboot -f";
                        # pri-lost-after-sb "/usr/lib/drbd/notify-pri-lost-after-sb.sh; /usr/lib/drbd/notify-emergency-reboot.sh; echo b > /proc/sysrq-trigger ; reboot -f";
                        # local-io-error "/usr/lib/drbd/notify-io-error.sh; /usr/lib/drbd/notify-emergency-shutdown.sh; echo o > /proc/sysrq-trigger ; halt -f";
                        # fence-peer "/usr/lib/drbd/crm-fence-peer.sh";
                        # split-brain "/usr/lib/drbd/notify-split-brain.sh root";
                        # out-of-sync "/usr/lib/drbd/notify-out-of-sync.sh root";
                        # before-resync-target "/usr/lib/drbd/snapshot-resync-target-lvm.sh -p 15 -- -c 16k";
                        # after-resync-target /usr/lib/drbd/unsnapshot-resync-target-lvm.sh;
                        # quorum-lost "/usr/lib/drbd/notify-quorum-lost.sh root";
                }
        
                startup {
                        # wfc-timeout degr-wfc-timeout outdated-wfc-timeout wait-after-sb
                }
        
                options {
                        # cpu-mask on-no-data-accessible
        
                        # RECOMMENDED for three or more storage nodes with DRBD 9:
                        # quorum majority;
                        # on-no-quorum suspend-io | io-error;
                }
        
                disk {
                        # size on-io-error fencing disk-barrier disk-flushes
                        # disk-drain md-flushes resync-rate resync-after al-extents
                        # c-plan-ahead c-delay-target c-fill-target c-max-rate
                        # c-min-rate disk-timeout
                }
        
                net {
                        # protocol timeout max-epoch-size max-buffers
                        # connect-int ping-int sndbuf-size rcvbuf-size ko-count
                        # allow-two-primaries cram-hmac-alg shared-secret after-sb-0pri
                        # after-sb-1pri after-sb-2pri always-asbp rr-conflict
                        # ping-timeout data-integrity-alg tcp-cork on-congestion
                        # congestion-fill congestion-extents csums-alg verify-alg
                        # use-rle
                }
        }
       ```

      drbd.conf 文件
  
      ```bash
        # You can find an example in  /usr/share/doc/drbd.../drbd.conf.example
        
        include "drbd.d/global_common.conf";
        include "drbd.d/*.res";  
      ```
  
  d. 加载内核

      ```bash
         insmod drbd.ko drbd_transport_tcp.ko
      ```

### 编译 drbd-tools

```bash
git clone -n https://github.com/LINBIT/drbd-utils.git
cd drbd-utils
git checkout v9.12.1
git clone -n https://github.com/LINBIT/drbd-headers.git
cd drbd-headers/
git checkout c757cf357edef67751b8f45a6ea894d287180087
cd ..
#安装依赖
yum install -y build-essential wget flex automake
  
./autogen.sh
./configure --prefix=/usr --localstatedir=/var --sysconfdir=/etc
make tools
find ./user -type f -executable -name 'drbd[a-z]*' -exec mv -v {} /usr/local/bin/ \;
```

### 进行验证

```bash
$ drbdadm -V

DRBDADM_BUILDTAG=GIT-hash:\ 6aec3180805d84f142f422013810af10cf4f95acdrbd-headers\ build\ by\ @buildkitsandbox\,\ 2022-10-12\ 10:40:34
DRBDADM_API_VERSION=2
DRBD_KERNEL_VERSION_CODE=0x090020
DRBD_KERNEL_VERSION=9.0.32
DRBDADM_VERSION_CODE=0x090c01
DRBDADM_VERSION=9.12.1
```
