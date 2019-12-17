namespace GotoWork_PC_v1._0
{
	partial class Form_Main
	{
		/// <summary>
		/// 필수 디자이너 변수입니다.
		/// </summary>
		private System.ComponentModel.IContainer components = null;

		/// <summary>
		/// 사용 중인 모든 리소스를 정리합니다.
		/// </summary>
		/// <param name="disposing">관리되는 리소스를 삭제해야 하면 true이고, 그렇지 않으면 false입니다.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing && (components != null))
			{
				components.Dispose();
			}
			base.Dispose(disposing);
		}

		#region Windows Form 디자이너에서 생성한 코드

		/// <summary>
		/// 디자이너 지원에 필요한 메서드입니다. 
		/// 이 메서드의 내용을 코드 편집기로 수정하지 마세요.
		/// </summary>
		private void InitializeComponent()
		{
			this.btn_leavework = new System.Windows.Forms.Button();
			this.btn_attendance = new System.Windows.Forms.Button();
			this.textbox_name = new System.Windows.Forms.TextBox();
			this.label_time = new System.Windows.Forms.Label();
			this.label_date = new System.Windows.Forms.Label();
			this.label_title = new System.Windows.Forms.Label();
			this.pictureBox1 = new System.Windows.Forms.PictureBox();
			((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
			this.SuspendLayout();
			// 
			// btn_leavework
			// 
			this.btn_leavework.Font = new System.Drawing.Font("서울남산체 M", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
			this.btn_leavework.Location = new System.Drawing.Point(12, 295);
			this.btn_leavework.Name = "btn_leavework";
			this.btn_leavework.Size = new System.Drawing.Size(216, 41);
			this.btn_leavework.TabIndex = 0;
			this.btn_leavework.Text = "퇴근";
			this.btn_leavework.UseVisualStyleBackColor = true;
			// 
			// btn_attendance
			// 
			this.btn_attendance.Font = new System.Drawing.Font("서울남산체 M", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
			this.btn_attendance.Location = new System.Drawing.Point(12, 249);
			this.btn_attendance.Name = "btn_attendance";
			this.btn_attendance.Size = new System.Drawing.Size(216, 41);
			this.btn_attendance.TabIndex = 1;
			this.btn_attendance.Text = "출근";
			this.btn_attendance.UseVisualStyleBackColor = true;
			// 
			// textbox_name
			// 
			this.textbox_name.Font = new System.Drawing.Font("서울남산체 M", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
			this.textbox_name.Location = new System.Drawing.Point(12, 217);
			this.textbox_name.Name = "textbox_name";
			this.textbox_name.Size = new System.Drawing.Size(216, 26);
			this.textbox_name.TabIndex = 2;
			this.textbox_name.Text = "이름";
			this.textbox_name.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
			// 
			// label_time
			// 
			this.label_time.AutoSize = true;
			this.label_time.Font = new System.Drawing.Font("서울남산체 M", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
			this.label_time.Location = new System.Drawing.Point(101, 190);
			this.label_time.Name = "label_time";
			this.label_time.Size = new System.Drawing.Size(38, 19);
			this.label_time.TabIndex = 3;
			this.label_time.Text = "시간";
			this.label_time.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// label_date
			// 
			this.label_date.AutoSize = true;
			this.label_date.Font = new System.Drawing.Font("서울남산체 M", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
			this.label_date.Location = new System.Drawing.Point(101, 158);
			this.label_date.Name = "label_date";
			this.label_date.Size = new System.Drawing.Size(39, 19);
			this.label_date.TabIndex = 4;
			this.label_date.Text = "날짜";
			this.label_date.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// label_title
			// 
			this.label_title.AutoSize = true;
			this.label_title.Font = new System.Drawing.Font("서울남산체 M", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(129)));
			this.label_title.Location = new System.Drawing.Point(80, 129);
			this.label_title.Name = "label_title";
			this.label_title.Size = new System.Drawing.Size(81, 19);
			this.label_title.TabIndex = 5;
			this.label_title.Text = "GotoWork";
			this.label_title.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// pictureBox1
			// 
			this.pictureBox1.Image = global::GotoWork_PC_v1._0.Properties.Resources.bella_logo;
			this.pictureBox1.Location = new System.Drawing.Point(13, 13);
			this.pictureBox1.Name = "pictureBox1";
			this.pictureBox1.Size = new System.Drawing.Size(215, 99);
			this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
			this.pictureBox1.TabIndex = 6;
			this.pictureBox1.TabStop = false;
			// 
			// Form_Main
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(240, 344);
			this.Controls.Add(this.pictureBox1);
			this.Controls.Add(this.label_title);
			this.Controls.Add(this.label_date);
			this.Controls.Add(this.label_time);
			this.Controls.Add(this.textbox_name);
			this.Controls.Add(this.btn_attendance);
			this.Controls.Add(this.btn_leavework);
			this.Name = "Form_Main";
			this.Text = "GotoWork_PC";
			((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Button btn_leavework;
		private System.Windows.Forms.Button btn_attendance;
		private System.Windows.Forms.TextBox textbox_name;
		private System.Windows.Forms.Label label_time;
		private System.Windows.Forms.Label label_date;
		private System.Windows.Forms.Label label_title;
		private System.Windows.Forms.PictureBox pictureBox1;
	}
}

